from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
DATABASE = 'database.db'


# ---------------- DB INIT ----------------
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                due TEXT NOT NULL,
                priority TEXT NOT NULL,
                repeat INTEGER NOT NULL,
                completed INTEGER NOT NULL
            )
        ''')
        conn.commit()


# ---------------- RECURRING TASKS ----------------
def recreate_recurring_tasks():
    try:
        with sqlite3.connect(DATABASE) as conn:
            recurring_tasks = conn.execute(
                'SELECT * FROM tasks WHERE repeat = 1 AND completed = 1'
            ).fetchall()

            for task in recurring_tasks:
                due_date = datetime.strptime(task[2], '%Y-%m-%d %H:%M:%S')
                new_due_date = due_date + timedelta(days=7)

                conn.execute('''
                    INSERT INTO tasks (name, due, priority, repeat, completed)
                    VALUES (?, ?, ?, ?, ?)
                ''', (
                    task[1],
                    new_due_date.strftime('%Y-%m-%d %H:%M:%S'),
                    task[3],
                    task[4],
                    0
                ))

            conn.commit()
    except Exception as e:
        print("Scheduler Error:", e)


# ---------------- SCHEDULER ----------------
scheduler = BackgroundScheduler()
scheduler.add_job(recreate_recurring_tasks, 'interval', hours=1)
scheduler.start()


# ---------------- HOME ROUTE ----------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- TASKS API ----------------
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    with sqlite3.connect(DATABASE) as conn:

        if request.method == 'POST':
            data = request.json

            cursor = conn.execute('''
                INSERT INTO tasks (name, due, priority, repeat, completed)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                data['name'],
                data['due'],
                data['priority'],
                int(data['repeat']),
                0
            ))

            conn.commit()

            task_id = cursor.lastrowid

            return jsonify({
                'id': task_id,
                'name': data['name'],
                'due': data['due'],
                'priority': data['priority'],
                'repeat': bool(data['repeat']),
                'completed': False
            }), 201


        # GET REQUEST
        priority = request.args.get('priority')
        sort = request.args.get('sort')

        query = "SELECT * FROM tasks"
        params = []

        if priority:
            query += " WHERE priority = ?"
            params.append(priority)

        if sort == 'date':
            query += " ORDER BY due"
        elif sort == 'priority':
            query += " ORDER BY priority DESC"

        rows = conn.execute(query, params).fetchall()

        tasks_list = [
            {
                'id': r[0],
                'name': r[1],
                'due': r[2],
                'priority': r[3],
                'repeat': bool(r[4]),
                'completed': bool(r[5])
            }
            for r in rows
        ]

        return jsonify(tasks_list)


# ---------------- TOGGLE COMPLETE ----------------
@app.route('/tasks/<int:id>/complete', methods=['PUT'])
def complete_task(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute(
            'UPDATE tasks SET completed = CASE WHEN completed=1 THEN 0 ELSE 1 END WHERE id=?',
            (id,)
        )
        conn.commit()

    return jsonify({"message": "Task status updated"})


# ---------------- DELETE TASK ----------------
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
        conn.commit()

    return jsonify({"message": "Task deleted"})


# ---------------- START APP ----------------
if __name__ == '__main__':
    init_db()
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )