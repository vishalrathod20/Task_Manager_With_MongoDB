# Task Manager with MongoDB

## Description
The **Task Manager** is a command-line-based project that helps users manage their tasks using MongoDB as the database. It allows users to create, view, update, and delete tasks, each with a priority level (Low, Medium, High) and status (Pending or Completed). The tasks are stored in a MongoDB database called `todo_db` within a collection called `tasks`.

## Key Features
1. **Create Task**: Users can create new tasks by specifying a description and setting a priority level (Low, Medium, or High). Each task is assigned a default status of "Pending."
2. **View Tasks**: Users can view a list of all tasks with their ID, description, status, and priority.
3. **Mark Task as Completed**: Users can mark specific tasks as completed by providing the corresponding task ID.
4. **Delete Task**: Users can delete tasks from the list by providing the task's unique ID.
5. **Persistence**: All tasks are stored in a MongoDB collection, ensuring that task data persists between program executions.

## How it Works
- The project connects to a MongoDB instance running locally.
- Users are presented with a menu that allows them to manage their tasks.
- Each task is stored as a document in the MongoDB collection, with fields for the task description, status, and priority.
- Users interact with the MongoDB database using basic CRUD operations (Create, Read, Update, Delete). 

This project provides a simple and practical way to manage daily tasks through a database-backed command-line interface.
