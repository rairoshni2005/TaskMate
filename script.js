document.addEventListener('DOMContentLoaded', () => {
  loadTasks(); // Load tasks when the page loads
  setupThemeToggle(); // Set up the theme toggle button
  checkReminders(); // Start checking for reminders
  requestNotificationPermission(); // Request notification permission
});

// Save a new task
const taskForm = document.getElementById('task-form');
taskForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const taskName = document.getElementById('task-name').value;
  const taskDue = document.getElementById('task-due').value;
  const taskPriority = document.getElementById('task-priority').value;
  const taskRepeat = document.getElementById('task-repeat').checked;

  const task = {
    name: taskName,
    due: taskDue,
    priority: taskPriority,
    repeat: taskRepeat,
    completed: false
  };

  saveTask(task);
  taskForm.reset();
});

// Save task to the backend
function saveTask(task) {
  fetch('/tasks', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(task)
  })
    .then(response => response.json())
    .then(data => {
      console.log('Task saved:', data);
      loadTasks(); // Reload tasks after saving
    })
    .catch(error => console.error('Error saving task:', error));
}

// Load tasks from the backend
function loadTasks() {
  fetch('/tasks')
    .then(response => response.json())
    .then(tasks => {
      const taskList = document.getElementById('task-list');
      taskList.innerHTML = ''; // Clear the task list
      tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
          <span>${task.name} (${task.priority}) - Due: ${new Date(task.due).toLocaleString()}</span>
          <div class="task-buttons">
            <button onclick="toggleComplete(${task.id})">${task.completed ? 'Undo' : 'Complete'}</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
          </div>
        `;
        taskList.appendChild(li);
      });
    })
    .catch(error => console.error('Error loading tasks:', error));
}

// Toggle task completion status
function toggleComplete(id) {
  fetch(`/tasks/${id}/complete`, { method: 'PUT' })
    .then(() => loadTasks()) // Reload tasks after toggling
    .catch(error => console.error('Error toggling task completion:', error));
}

// Delete a task
function deleteTask(id) {
  fetch(`/tasks/${id}`, { method: 'DELETE' })
    .then(() => loadTasks()) // Reload tasks after deletion
    .catch(error => console.error('Error deleting task:', error));
}

// Filter tasks by priority
function filterTasks(priority) {
  fetch(`/tasks?priority=${priority}`)
    .then(response => response.json())
    .then(tasks => {
      const taskList = document.getElementById('task-list');
      taskList.innerHTML = ''; // Clear the task list
      tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
          <span>${task.name} (${task.priority}) - Due: ${new Date(task.due).toLocaleString()}</span>
          <div class="task-buttons">
            <button onclick="toggleComplete(${task.id})">${task.completed ? 'Undo' : 'Complete'}</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
          </div>
        `;
        taskList.appendChild(li);
      });
    })
    .catch(error => console.error('Error filtering tasks:', error));
}

// Sort tasks by criteria (date or priority)
function sortTasks(criteria) {
  fetch(`/tasks?sort=${criteria}`)
    .then(response => response.json())
    .then(tasks => {
      const taskList = document.getElementById('task-list');
      taskList.innerHTML = ''; // Clear the task list
      tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';
        li.innerHTML = `
          <span>${task.name} (${task.priority}) - Due: ${new Date(task.due).toLocaleString()}</span>
          <div class="task-buttons">
            <button onclick="toggleComplete(${task.id})">${task.completed ? 'Undo' : 'Complete'}</button>
            <button onclick="deleteTask(${task.id})">Delete</button>
          </div>
        `;
        taskList.appendChild(li);
      });
    })
    .catch(error => console.error('Error sorting tasks:', error));
}

// Set up the theme toggle button
function setupThemeToggle() {
  const themeToggle = document.getElementById('theme-toggle');
  const body = document.body;

  // Set initial theme based on localStorage or default to light mode
  const savedTheme = localStorage.getItem('theme') || 'light';
  body.dataset.theme = savedTheme;
  themeToggle.textContent = savedTheme === 'dark' ? 'Light Mode' : 'Dark Mode';

  // Toggle theme on button click
  themeToggle.addEventListener('click', () => {
    const newTheme = body.dataset.theme === 'dark' ? 'light' : 'dark';
    body.dataset.theme = newTheme;
    themeToggle.textContent = newTheme === 'dark' ? 'Light Mode' : 'Dark Mode';
    localStorage.setItem('theme', newTheme);
  });
}

// Check for reminders
function checkReminders() {
  fetch('/tasks')
    .then(response => response.json())
    .then(tasks => {
      tasks.forEach(task => {
        const dueDate = new Date(task.due);
        const now = new Date();
        const timeDiff = dueDate - now;

        if (timeDiff > 0 && timeDiff <= 3600000) { // 1 hour before due
          if (Notification.permission === 'granted') {
            new Notification('TaskMate Reminder', {
              body: `Task "${task.name}" is due soon!`,
            });
          }
        }
      });
    });
}

// Request notification permission
function requestNotificationPermission() {
  if (Notification.permission !== 'granted') {
    Notification.requestPermission();
  }
}

// Check reminders every minute
setInterval(checkReminders, 60000);