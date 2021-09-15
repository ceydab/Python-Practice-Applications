import mysql.connector
import passwordsql from logins

class SchoolDatabase():
    def __init__(self):
        self.connection = mysql.connector.connect(host= "localhost", user = "root", password = passwordsql, database = "schooldb" )
        self.cursor = self.connection.cursor()

    def initApp(self):
        menu = int(input("1-Students \n2-Teachers \n3-Classes \n4-Lessons \nSelect: "))
        while True:
            if menu == 1:
                menuSt = int(input("1-Show students \n2-Insert student \n3-Update student \n4-Delete student \n5-Exit\nSelect:"))
                if menuSt == 1:
                    self.displayStudent()
                elif menuSt ==2 :
                    self.insertStudent()
                elif menuSt == 3 :
                    self.updateStudent()
                elif menuSt ==4:
                    self.deleteStudent()
                elif menuSt ==5:
                    break
                else:
                    print(menuSt)

            if menu == 2:
                menuSt = int(input("1-Show teachers \n2-Insert teacher \n3-Update teacher \n4-Delete teacher \n5-Exit\nSelect:"))
                if menuSt == 1:
                    self.displayTeacher()
                elif menuSt ==2 :
                    self.insertTeacher()
                elif menuSt == 3 :
                    self.updateTeacher()
                elif menuSt ==4:
                    self.deleteTeacher()
                elif menuSt ==5:
                    break
                else:
                    print(menuSt)

            if menu == 3:
                menuSt = int(input("1-Show classes \n2-Insert class \n3-Update class \n4-Delete class \n5-Exit\nSelect:"))
                if menuSt == 1:
                    self.displayClasses()
                elif menuSt ==2 :
                    self.insertClasses()
                elif menuSt == 3 :
                    self.updateClasses()
                elif menuSt ==4:
                    self.deleteClasses()
                elif menuSt ==5:
                    break
                else:
                    print(menuSt)

            if menu == 4:
                menuSt = int(input("1-Show lessons \n2-Insert lesson \n3-Update lesson \n4-Delete lesson \n5-Exit\nSelect:"))
                if menuSt == 1:
                    self.displayLessons()
                elif menuSt ==2 :
                    self.insertLessons()
                elif menuSt == 3 :
                    self.updateLessons()
                elif menuSt ==4:
                    self.deleteLessons()
                elif menuSt ==5:
                    break
                else:
                    print(menuSt)



    def createDatabase(self):
        self.cursor.execute("CREATE DATABASE schooldb") 
        self.cursor.execute("CREATE TABLE Student(id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,studentNumber INT UNIQUE NOT NULL,name VARCHAR(20) NOT NULL,surname VARCHAR(20) NOT NULL,classid INT NOT NULL)") 
        self.cursor.execute("CREATE TABLE Teacher(id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,branch VARCHAR(20) NOT NULL,name VARCHAR(20) NOT NULL,surname VARCHAR(20) NOT NULL,classid INT NOT NULL)") 
        self.cursor.execute("CREATE TABLE Class(id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,name VARCHAR(20) NOT NULL,teacherid INT NOT NULL)") 
        self.cursor.execute("CREATE TABLE Lesson(id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,name VARCHAR(20) NOT NULL)") 
        self.cursor.execute("CREATE TABLE ClassLesson(id INT UNIQUE PRIMARY KEY NOT NULL,classid INT NOT NULL,lessonid INT NOT NULL,teacherid INT NOT NULL)") 
        self.cursor.execute("ALTER TABLE Student Add constraint fk_Class_Student FOREIGN KEY (classid) REFERENCES Class(id)") 
        self.cursor.execute("ALTER TABLE Teacher ADD constraint fk_class_teacher FOREIGN KEY (classid) REFERENCES class (id)") 
        self.cursor.execute("ALTER TABLE Class ADD constraint fk_teacher_class FOREIGN KEY (teacherid) REFERENCES teacher (id)") 
        self.cursor.execute("ALTER TABLE classlesson ADD constraint fk_class_classlesson FOREIGN KEY (classid) REFERENCES class (id)") 
        self.cursor.execute("ALTER TABLE classlesson ADD constraint fk_teacher_classlesson FOREIGN KEY (teacherid) REFERENCES teacher (id)") 
        self.cursor.execute("ALTER TABLE classlesson ADD constraint fk_lesson_classlesson FOREIGN KEY (lessonid) REFERENCES lesson (id)") 
        


    def displayStudent(self):
        self.cursor.execute("SELECT * FROM Student")
        obj = self.cursor.fetchall()
        try:
            print(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def insertStudent(self):
        studentno = int(input("Student no: "))
        studentname = input("Student name: ")
        studentsurname = input("Student surname: ")
        studentclassid = int(input("Student classid: "))
        sql = ("INSERT INTO Student(studentNumber, name, surname, classid) VALUES(%s,%s,%s,%s)")
        values = (studentno, studentname, studentsurname, studentclassid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} students added.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def updateStudent(self):
        studentid = int(input("Student id: "))
        studentno = int(input("Student no: "))
        studentname = input("Student name: ")
        studentsurname = input("Student surname: ")
        studentclassid = int(input("Student classid: "))
        sql = ("UPDATE Student set studentNumber= %s, name = %s, surname = %s, classid = %s where id=%s")
        values = (studentno, studentname, studentsurname, studentclassid, studentid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} students updated.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def deleteStudent(self):
        studentid = int(input("Student id: "))
        sql = ("DELETE from Student where id = %s")
        values = (studentid,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} students deleted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def displayTeacher(self):
        self.cursor.execute("SELECT * FROM Teacher")
        obj = self.cursor.fetchall()
        try:
            print(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def insertTeacher(self):
        teachername = input("Teacher name: ")
        teachersurname = input("Teacher surname: ")
        teacherbranch = input("Branch: ")
        teacherclassid = int(input("Teacher classid: "))
        sql = ("INSERT INTO Teacher(name, surname, branch, classid) VALUES(%s,%s,%s,%s)")
        values = (teachername, teachersurname, teacherbranch, teacherclassid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} teachers added.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")
    def updateTeacher(self):
        teacherid = int(input("Teacher id: "))
        teachername = input("Teacher name: ")
        teachersurname = input("Teacher surname: ")
        teacherbranch = input("Branch: ")
        teacherclassid = int(input("Teacher classid: "))
        sql = ("UPDATE Teacher set name = %s, surname = %s, branch = %s, classid = %s where id=%s")
        values = (teachername, teachersurname, teacherbranch, teacherclassid, teacherid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} teachers updated.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def deleteTeacher(self):
        teacherid = int(input("Teacher id: "))
        sql = ("DELETE from Teacher where id = %s")
        values = (teacherid,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} teachers deleted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def displayLessons(self):
        self.cursor.execute("SELECT * FROM lesson")
        obj = self.cursor.fetchall()
        try:
            print(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def insertLessons(self):
        lessonname = input("Lesson name: ")
        sql = ("INSERT INTO lesson(name) VALUES(%s)")
        values = (lessonname,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} lessons added.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def updateLessons(self):
        lessonname = input("Lesson name: ")
        lessonid = int(input("Lesson id: "))
        sql = ("UPDATE lesson set name = %s where id=%s")
        values = (lessonname, lessonid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} lessons updated.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def deleteLessons(self):
        lessonid = int(input("Lesson id: "))
        sql = ("DELETE from lesson where id=%s")
        values = (lessonid,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} lessons deleted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def displayClasses(self):
        self.cursor.execute("SELECT * FROM class")
        obj = self.cursor.fetchall()
        try:
            print(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def insertClasses(self):
        classname = input("Class: ")
        classteacherid = int(input("Teacher id:"))
        sql = ("INSERT INTO class(name,teacherid) VALUES(%s,%s)")
        values = (classname,classteacherid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} classes added.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")


    def updateClasses(self):
        classname = input("Class: ")
        classteacherid = int(input("Teacher id:"))
        classid = int(input("Class id:"))
        sql = ("UPDATE class set name = %s , teacherid = %s where id=%s")
        values = (classname,classteacherid, classid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} classes updated.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def deleteClasses(self):
        classid = int(input("Class id:"))
        sql = ("DELETE from class where id=%s")
        values = (classid,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} classes deleted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def displayClassLessons(self):
        self.cursor.execute("SELECT * FROM classlesson")
        obj = self.cursor.fetchall()
        try:
            print(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def insertClassLessons(self):
        classid = int(input("Class id:"))
        lessonid = int(input("Lesson id: "))
        teacherid = int(input("Teacher id: "))
        sql = ("INSERT INTO classlesson(classid, lessonid, teacherid) VALUES(%s,%s,%s)")
        values = (classid, lessonid, teacherid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} class-lesson matched.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def updateClassLessons(self):
        classid = int(input("Class id:"))
        lessonid = int(input("Lesson id: "))
        teacherid = int(input("Teacher id: "))
        matchid = int(input("Match id:"))
        sql = ("UPDATE classlesson set classid=%s, lessonid=%s, teacherid=%s where id=%s")
        values = (classid, lessonid, teacherid, matchid)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} class-lesson updated.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

    def deleteClassLessons(self):
        matchid = int(input("Match id:"))
        sql = ("DELETE from classlesson where id=%s")
        values = (matchid,)
        self.cursor.execute(sql,values)
        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} class-lesson match deleted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            print("Process completed")

SchoolDatabase()
SchoolDatabase().initApp()
