window.onload() = function() {
    console.log('Page loaded');
    try {
        const response = fetch('/tasks/tasks', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
              },
        });
        if (!response.ok) {
            throw new Error('Failed to fetch tasks');
        }

        const tasks = response.json();
        const taskList = document.querySelector('#taskList');

        taskList.innerHTML = '';
        tasks.forEach(task => renderTask(task, taskList));
        
    }
    catch (error) {
        console.error('Error in fetching tasks', error);
    }
}

// Render the task into li
function renderTask(task, taskList) {
    const taskItem = document.createElement('li');
    taskItem.id = `task-id${task.id}`;
    taskItem.innerHTML = `
        <h2>${task.title.toUpperCase()}</h2>
        <p>${task.description}</p>
        <!-- <p>{{ task.task_due_date }}</p> -->
        <p> ${task.completed}</p>
        ${task.completed !== true ? `
            <button id="status-btn-{{ task.id }}" onclick="markedCompleted('{{task.id}}')">Mark as Complete</button>
        ` : ''}
        <a href="{{ url_for('tasks.edit_task', task_id=task.id) }}"><button>Edit Task</button></a>
    `;
    taskList.appendChild(taskItem);
}

// async function markedCompleted(id) {
//     try {
//         const response = await fetch('/tasks', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({ task_id: id }),
//         });
//         const data = await response.json();
//         console.log(id);
//         if (response.ok) {
//             alert(`Task ${data.task_id} marked as completed!`);
//             // Optionally refresh the task list or update the UI
//             var status = document.createElement('p');
//             status.innerHTML = `${data.status}`;
//             document.querySelector(`#btn-container-${data.task_id}`).innerHTML = '';
//             document.querySelector(`#btn-container-${data.task_id}`).appendChild(status);
//         } else {
//             alert(data.error || 'Failed to mark task as complete');
//         }
//     } catch (error) {
//         console.error('Error:', error);
//         alert('Something went wrong!');
//     }
// }