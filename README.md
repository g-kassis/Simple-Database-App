# Simple-Database-App

# Objective
Implement a PostgreSQL database using the provided schema and write an application in your language of choice that connects to this database to perform specific CRUD (Create, Read, Update, Delete) operations.

# Documentation
Retrieves and displays all records from the students table.
```
getAllStudents():
```
Inserts a new student record into the students table.
```
addStudent(first_name, last_name, email, enrollment_date): 
```
Updates the email address for a student with the specified student_id.
```
updateStudentEmail(student_id, new_email): 
```
Deletes the record of the student with the specified student_id.
```
deleteStudent(student_id): 
```

<br>

[Demo Video](https://drive.google.com/file/d/1fcaQ9Xo-oOSf4U2G4SXcuXqOufNY87uO/view?usp=sharing)


# How To Run
Install psycopg2 Python package:
```
pip install psycopg2
```
Run app.py using Python3:
```
python3 app.py
```
Follow instructions on screen


# Technologies

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
