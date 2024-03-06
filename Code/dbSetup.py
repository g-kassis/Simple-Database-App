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