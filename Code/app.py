import psycopg2 as pg


#Establishes connection to PostgresSQL
psql = pg.connect(
    host = 'localhost',
    user = 'postgres',
    password = 'postgres',
)
client = psql.cursor()
psql.set_isolation_level(pg.extensions.ISOLATION_LEVEL_AUTOCOMMIT)


try:
    #Creates database "Assignment3"
    client.execute("CREATE DATABASE assignment3")
    #reconnect to the newly created database
    psql = pg.connect(host = 'localhost', database = 'assignment3', user = 'postgres', password = 'postgres',)      
    client = psql.cursor()    

except:
    print('Database exists')
    #reconnect to the newly created database
    psql = pg.connect(host = 'localhost', database = 'assignment3', user = 'postgres', password = 'postgres',)        
    client = psql.cursor()

try:
    #Creates table with first_name, last_name, email, enrollment_date columns
    client.execute("CREATE Table students(student_id SERIAL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, enrollment_date DATE)")

except:
    #drops table if it exists and recreates it
    psql.rollback()
    print('Table exists -- Dropping table and re-creating')
    client.execute("DROP TABLE students")
    client.execute("CREATE Table students(student_id SERIAL PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, enrollment_date DATE)")

#Inserts Data into students table
client.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('John', 'Doe','john.doe@example.com', '2023-09-01'),('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')") 

psql.commit() 


#Retrieves and displays all records from the students table
def getAllStudents():
    try: 
        client.execute("SELECT * FROM students")
        results = client.fetchall()
        printData(results)
    except:
        print('Error: could not SELECT FROM table')


#Inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        client.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        psql.commit()
    except:
        print('Error: could not INSERT INTO table')

#Updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email): 
    try:
        client.execute("UPDATE students SET email = %s WHERE student_id = %s",(new_email,student_id))
        psql.commit()
    except:
        print('Error: could not UPDATE in table')


#Deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    try: 
        client.execute("DELETE FROM students WHERE student_id = %s",student_id)
        psql.commit()
    except:
        print('Error: could not DELETE in table')

#helper function that prints all rows in a clean way
def printData(data):
    # Define the updated column headers
    headers = ['student_id', 'first_name', 'last_name', 'email', 'enrollment_date']
    column_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]

    header_format = ' | '.join(['{:<' + str(width) + '}' for width in column_widths])
    print(header_format.format(*headers))

    separator_line = '-+-'.join(['-' * width for width in column_widths])
    print(separator_line)

    row_format = ' | '.join(['{:<' + str(width) + '}' for width in column_widths])
    for row in data:
        print(row_format.format(*map(str, row)))
    print('\n')


#main while loop for the program 
while (True):

    userInput = input('Select a function: \n 1.getAllStudents\n 2.addStudent\n 3.updateStudentEmail\n 4.deleteStudent \n q - to quit: \n\n$')

    if userInput == '1' or userInput == 'getAllStudents':
        getAllStudents()

    elif userInput == '2' or userInput == 'addStudent':
        functionInput = input('Please provide the first_name, last_name, email, enrollment_date of the new student(seperated by a comma) \nenrollment_date format (YYYY-MM-DD):\n$')
        noSpace = functionInput.strip(' ')
        firstName, lastName, email, enrollment = noSpace.split(',')
        addStudent(firstName.strip(' '), lastName.strip(' '), email.strip(' '), enrollment.strip(' '))

    elif userInput == '3' or userInput == 'updateStudentEmail':
        functionInput = input('Please provide the student_id and the new email to update (seperated by a comma): \n$')
        noSpace = functionInput.strip(' ')
        studentID, newEmail = noSpace.split(',')
        updateStudentEmail(studentID.strip(' '), newEmail.strip(' '))

    elif userInput == '4' or userInput == 'deleteStudent':
        functionInput = input('Please provide the student_id to be deleted: \n$')
        deleteStudent(1)
    
    elif userInput == 'q' or userInput == 'Q':
        client.close()
        psql.close()
        break

    else:
        print('Unknown function or input')

