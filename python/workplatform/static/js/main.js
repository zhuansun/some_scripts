document.addEventListener('DOMContentLoaded', function() {
    loadTasks();
    
    // 显示添加任务弹窗
    document.getElementById('show-add-task').addEventListener('click', function() {
        document.getElementById('task-form-modal').style.display = 'flex';
    });
    
    // 取消添加任务
    document.getElementById('cancel-add-task').addEventListener('click', function() {
        document.getElementById('task-form-modal').style.display = 'none';
        document.getElementById('add-task-form').reset();
    });
    
    // 添加任务表单提交
    document.getElementById('add-task-form').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const quadrant = document.getElementById('quadrant').value;
        
        addTask(title, description, quadrant);
        
        // 重置表单并关闭弹窗
        this.reset();
        document.getElementById('task-form-modal').style.display = 'none';
    });
    
    // 关闭任务详情
    document.getElementById('close-details').addEventListener('click', function() {
        document.getElementById('task-details').style.display = 'none';
        document.getElementById('overlay').style.display = 'none';
    });
    
    // 完成任务
    document.getElementById('complete-task').addEventListener('click', function() {
        const taskId = document.getElementById('task-details').dataset.taskId;
        completeTask(taskId);
    });
    
    // 删除任务
    document.getElementById('delete-task').addEventListener('click', function() {
        const taskId = document.getElementById('task-details').dataset.taskId;
        deleteTask(taskId);
    });
});

// 加载任务
function loadTasks() {
    fetch('/api/tasks')
        .then(response => response.json())
        .then(tasks => {
            // 清空所有象限
            document.querySelectorAll('.quadrant').forEach(quadrant => {
                const children = Array.from(quadrant.children);
                children.forEach(child => {
                    if (!child.tagName || child.tagName.toLowerCase() !== 'h2') {
                        quadrant.removeChild(child);
                    }
                });
            });
            
            // 添加活跃的任务
            tasks.filter(task => task.status === 'active').forEach(task => {
                createTaskBubble(task);
            });
        })
        .catch(error => console.error('Error loading tasks:', error));
}

// 添加任务
function addTask(title, description, quadrant) {
    const task = {
        title,
        description,
        quadrant
    };
    
    fetch('/api/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(task)
    })
    .then(response => response.json())
    .then(newTask => {
        createTaskBubble(newTask);
    })
    .catch(error => console.error('Error adding task:', error));
}

// 创建任务气泡
function createTaskBubble(task) {
    const quadrant = document.getElementById(task.quadrant);
    const bubble = document.createElement('div');
    bubble.className = `task-bubble ${task.quadrant}`;
    bubble.textContent = task.title;
    bubble.dataset.taskId = task.id;
    
    // 计算气泡大小（基于创建时间）
    const createdDate = new Date(task.created_at);
    const now = new Date();
    const ageInDays = (now - createdDate) / (1000 * 60 * 60 * 24);
    const minSize = 60; // 最小尺寸（像素）
    const maxSize = 150; // 最大尺寸（像素）
    const size = Math.min(minSize + ageInDays * 5, maxSize);
    
    bubble.style.width = `${size}px`;
    bubble.style.height = `${size}px`;
    
    // 随机位置（避免重叠）
    const quadrantRect = quadrant.getBoundingClientRect();
    const maxLeft = quadrantRect.width - size;
    const maxTop = quadrantRect.height - size;
    
    bubble.style.left = `${Math.random() * maxLeft}px`;
    bubble.style.top = `${Math.random() * maxTop}px`;
    
    // 点击显示详情
    bubble.addEventListener('click', function() {
        showTaskDetails(task);
    });
    
    quadrant.appendChild(bubble);
}

// 显示任务详情
function showTaskDetails(task) {
    const detailsElement = document.getElementById('task-details');
    detailsElement.dataset.taskId = task.id;
    
    document.getElementById('detail-title').textContent = task.title;
    document.getElementById('detail-description').textContent = task.description || '无描述';
    
    const createdDate = new Date(task.created_at);
    document.getElementById('detail-created-at').textContent = createdDate.toLocaleString();
    
    document.getElementById('overlay').style.display = 'block';
    detailsElement.style.display = 'block';
}

// 完成任务
function completeTask(taskId) {
    fetch(`/api/tasks/${taskId}/complete`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('task-details').style.display = 'none';
        document.getElementById('overlay').style.display = 'none';
        loadTasks();
    })
    .catch(error => console.error('Error completing task:', error));
}

// 删除任务
function deleteTask(taskId) {
    fetch(`/api/tasks/${taskId}/delete`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('task-details').style.display = 'none';
        document.getElementById('overlay').style.display = 'none';
        loadTasks();
    })
    .catch(error => console.error('Error deleting task:', error));
} 