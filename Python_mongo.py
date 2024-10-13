from pymongo import MongoClient

# Connect to MongoDB
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

# Access database and collection
db = client.todo_db
task_collection = db.tasks

# Function to create a task with status and priority
def create_task(description, priority="Medium"):
    task = {
        'task': description,
        'status': 'Pending',  # Default status for new tasks
        'priority': priority   # Task priority
    }
    result = task_collection.insert_one(task)
    print(f'Task created with id: {result.inserted_id}')

# Function to view all tasks
def view_tasks():
    tasks = task_collection.find()
    if task_collection.count_documents({}) == 0:
        print("No tasks available.")
    else:
        print("\n--- Task List ---")
        for task in tasks:
            print(f"ID: {task['_id']} | Task: {task['task']} | Status: {task['status']} | Priority: {task['priority']}")

# Function to mark a task as completed
def mark_task_as_completed(task_id):
    result = task_collection.update_one({'_id': task_id}, {'$set': {'status': 'Completed'}})
    if result.modified_count > 0:
        print("Task marked as completed.")
    else:
        print("Task not found.")

# Function to delete a task
def delete_task(task_id):
    result = task_collection.delete_one({'_id': task_id})
    if result.deleted_count > 0:
        print("Task deleted.")
    else:
        print("Task not found.")

# Main loop
while True:
    print("\n1. Create Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter your task: ")
        priority = input("Enter priority (Low, Medium, High): ")
        create_task(description, priority)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        task_id = input("Enter task ID to mark as completed: ")
        try:
            from bson.objectid import ObjectId  # To handle MongoDB ObjectId
            mark_task_as_completed(ObjectId(task_id))
        except Exception as e:
            print(f"Error: {e}")
    elif choice == '4':
        task_id = input("Enter task ID to delete: ")
        try:
            from bson.objectid import ObjectId
            delete_task(ObjectId(task_id))
        except Exception as e:
            print(f"Error: {e}")
    elif choice == '5':
        break
    else:
        print("Please provide a valid option.")
