const tasksList = document.getElementById("tasksList");
const addBtn = document.getElementById("addBtn");
const taskInput = document.getElementById("taskInput");

// Load tasks
async function loadTasks() {
  tasksList.innerHTML = '';
  const res = await fetch('http://localhost:5000/tasks');
  const tasks = await res.json();

  tasks.forEach(task => {
    const li = document.createElement('li');
    li.className = task.completed ? 'completed' : '';
    li.innerHTML = `
      <span>${task.name}</span>
      <div>
        <button onclick="deleteTask(${task.id})">Delete</button>
        <button onclick="toggleComplete(${task.id})">${task.completed ? 'Undo' : 'Done'}</button>
      </div>
    `;
    tasksList.appendChild(li);
  });
}

// Add task
addBtn.addEventListener('click', async () => {
  const name = taskInput.value.trim();
  if(!name) return;
  await fetch('http://localhost:5000/tasks', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({ name })
  });
  taskInput.value = '';
  loadTasks();
});

// Delete task
async function deleteTask(id) {
  await fetch(`http://localhost:5000/tasks/${id}`, { method: 'DELETE' });
  loadTasks();
}

// Toggle completion
async function toggleComplete(id) {
  await fetch(`http://localhost:5000/tasks/${id}/toggle`, { method: 'PATCH' });
  loadTasks();
}

// Initial load
loadTasks();
