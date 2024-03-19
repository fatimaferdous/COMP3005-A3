import psycopg2 
#documentation: https://www.psycopg.org/docs/install.html

#linking .py file to database
link = psycopg2.connect("dbname=comp3005_A3 user=postgres password=3645 host=localhost port=5432")

cur = link.cursor()

#print out all students from the database
def getAllStudents():
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    for student in students:
        print(student)
        
#add a student to the database
def addStudent(first_name, last_name, email, enrollment_date):
    insert_query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)"
    cur.execute(insert_query, (first_name, last_name, email, enrollment_date))

#change or update an email based on student's id
def updateStudentEmail(student_id, new_email):
    update_query = "UPDATE students SET email = %s WHERE student_id = %s"
    cur.execute(update_query, (new_email, student_id))

#delete a student from database
def deleteStudent(student_id):
    delete_query = "DELETE FROM students WHERE student_id = %s"
    cur.execute(delete_query, (student_id))

#TESTING:

#just printing all students
#getAllStudents()

#adding student
#getAllStudents()
#addStudent("Fatima", "Ferdous", "fatimaferdous@cmail.carleton.ca", "2021-09-02")
#print("Updated:")
#getAllStudents()

#updating email
#getAllStudents() 
#updateStudentEmail(1, "new@gmail.com")
#print("Updated:")
#getAllStudents()

#deleting student
getAllStudents()
deleteStudent("1")
print("updated: ")
getAllStudents()

link.commit()
cur.close()
link.close()

