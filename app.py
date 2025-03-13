from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
DATABASE = 'database.db'

# Initialize the database
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

# Function to recreate recurring tasks
def recreate_recurring_tasks():
    with sqlite3.connect(DATABASE) as conn:
        recurring_tasks = conn.execute('SELECT * FROM tasks WHERE repeat = 1 AND completed = 1').fetchall()
        for task in recurring_tasks:
            due_date = datetime.strptime(task[2], '%Y-%m-%d %H:%M:%S')
            new_due_date = due_date + timedelta(days=7)
            conn.execute('''
                INSERT INTO tasks (name, due, priority, repeat, completed)
                VALUES (?, ?, ?, ?, ?)
            ''', (task[1], new_due_date.strftime('%Y-%m-%d %H:%M:%S'), task[3], task[4], 0))
            conn.commit()

# Schedule the recurring task check
scheduler = BackgroundScheduler()
scheduler.add_job(recreate_recurring_tasks, 'interval', hours=1)
scheduler.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        data = request.json
        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.execute('''
                INSERT INTO tasks (name, due, priority, repeat, completed)
                VALUES (?, ?, ?, ?, ?)
            ''', (data['name'], data['due'], data['priority'], int(data['repeat']), 0))
            conn.commit()
            task_id = cursor.lastrowid
            new_task = {
                'id': task_id,
                'name': data['name'],
                'due': data['due'],
                'priority': data['priority'],
                'repeat': bool(data['repeat']),
                'completed': False
            }
        return jsonify(new_task), 201

    priority = request.args.get('priority')
    sort = request.args.get('sort')
    query = 'SELECT * FROM tasks'
    if priority:
        query += f" WHERE priority = '{priority}'"
    if sort == 'date':
        query += ' ORDER BY due'
    elif sort == 'priority':
        query += ' ORDER BY priority DESC'
    with sqlite3.connect(DATABASE) as conn:
        tasks = conn.execute(query).fetchall()
        tasks = [dict(id=row[0], name=row[1], due=row[2], priority=row[3], repeat=bool(row[4]), completed=bool(row[5])) for row in tasks]
    return jsonify(tasks)

@app.route('/tasks/<int:id>/complete', methods=['PUT'])
def complete_task(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('UPDATE tasks SET completed = NOT completed WHERE id = ?', (id,))
        conn.commit()
    return jsonify({"message": "Task status updated"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
        conn.commit()
    return jsonify({"message": "Task deleted"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)