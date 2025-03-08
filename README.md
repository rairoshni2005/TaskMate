# 📌 TaskMate - Advanced To-Do App

TaskMate is a **simple yet powerful task management application** that helps users **track, organize, and complete** their tasks efficiently. With features like **weekly recurring tasks, reminders, and prioritization**, TaskMate ensures you never miss a deadline!

---

## 🔥 Features

- **✅ Add, Edit, Delete Tasks**: Easily manage your tasks with intuitive controls.
- **✅ Mark Tasks as Completed/Pending**: Keep track of your progress.
- **✅ Weekly Recurring Tasks**: Automatically recreate tasks every week.
- **✅ Reminder Notifications**: Get notified before a task is due.
- **✅ Task Prioritization (High/Medium/Low)**: Organize tasks by priority.
- **✅ Filter & Sort Tasks**: Filter by priority or sort by due date.
- **✅ Dark Mode**: Switch between light and dark themes for better readability.
- **✅ LocalStorage/Database Persistence**: Tasks are saved and persist across sessions.

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript (Vanilla JS)
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Notifications**: JavaScript alerts

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/RoshniRai7/taskmate.git
cd taskmate

2️⃣ Install Dependencies
Make sure you have Python 3.x installed. Then, install the required Python packages:

pip install -r requirements.txt

3️⃣ Run the Backend (Flask Server)
Start the Flask server:

python3 app.py

4️⃣ Open the App
Open index.html in your browser, or navigate to http://127.0.0.1:5000.

🎯 Usage
Add a New Task:

Enter a task name, due date, priority, and optionally enable weekly repetition.
Click "Add Task" to save it.
Manage Tasks:

Mark tasks as completed or pending.
Edit or delete tasks as needed.
Recurring Tasks:

Tasks with "Repeat Weekly" enabled will automatically reappear every 7 days.
Reminders:

Get browser notifications for tasks due within the next hour.
Filter & Sort:

Filter tasks by priority (High, Medium, Low).
Sort tasks by due date or priority.
Dark Mode:

Toggle between light and dark themes using the "Dark Mode" button.


📂 Project Structure

TaskMate/
├── static/
│   ├── css/
│   │   └── styles.css       # CSS for styling the app
│   └── js/
│       └── script.js        # JavaScript for frontend logic
├── templates/
│   └── index.html           # Main HTML file for the app
├── app.py                   # Flask backend (Python)
├── database.db              # SQLite database file
├── README.md                # Documentation
└── requirements.txt         # Python dependencies



🛠 Future Enhancements
🚀 Drag & Drop Task Sorting: Reorder tasks using drag-and-drop.
🚀 User Authentication: Add login/signup functionality.
🚀 Cloud Sync: Sync tasks across devices using cloud storage.
🚀 Mobile App Version: Build a mobile app for TaskMate.


👨‍💻 Contributors
Roshni Rai - GitHub Profile


📜 License
This project is licensed under the MIT License. See the LICENSE file for details.


🙌 Contributing
Contributions are welcome! If you'd like to contribute, please:


Fork the repository.
Create a new branch (git checkout -b feature/YourFeatureName).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeatureName).
Open a pull request.


❓ Support
If you encounter any issues or have questions, feel free to open an issue.
































