import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

#Create Students table with PRIMARY KEY and FOREIGN KEY constraints
cur.execute("CREATE TABLE Students (sid INTEGER PRIMARY KEY, sname TEXT, dept INTEGER, FOREIGN KEY (dept) REFERENCES Departments(did))")

#Create Departments table with PRIMARY KEY constraint
cur.execute("CREATE TABLE Departments (did INTEGER PRIMARY KEY, dname TEXT)")

#Insert data into Departments table
cur.execute("INSERT INTO Departments VALUES (15, 'Computer Engineering')")
cur.execute("INSERT INTO Departments VALUES (99, 'Industrial Engineering')")

#Insert data into Students table
cur.execute("INSERT INTO Students VALUES (11, 'Ahmet', 15)")
cur.execute("INSERT INTO Students VALUES (12, 'Ali', 15)")
cur.execute("INSERT INTO Students VALUES (13, 'Ayse', 99)")
cur.execute("INSERT INTO Students VALUES (14, 'Fatma', 15)")
cur.execute("INSERT INTO Students VALUES (15, 'Murat', 99)")

#Find the name of the Department with the maximum number of students
cur.execute("SELECT Departments.dname FROM Departments INNER JOIN Students ON Departments.did = Students.dept GROUP BY Departments.did ORDER BY COUNT(*) DESC LIMIT 1")
result = cur.fetchone()
if result:
    print(f"The department with the maximum number of students is {result[0]}")

con.close()