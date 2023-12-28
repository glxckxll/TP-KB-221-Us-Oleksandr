from student import *
from studentList import *
import csv

class Utils:

    @staticmethod

    def loadFile(file, studentList):
        with open(file, newline='') as csvFile:
            reader = csv.DictReader(csvFile)
            for row in reader:
                student = Student(row["name"], row["age"], row["course"], row["phone"])
                studentList.addStudent(student)
        return studentList

    @staticmethod

    def saveFile(file, studentList):
            
            with open(file, 'w', newline="") as SaveFile:
                fieldnames = ["name", "age", "course", "phone"]
                writer = csv.DictWriter(SaveFile, fieldnames=fieldnames)
                writer.writeheader()
                for student in studentList.students:
                    writer.writerow({"name": student.name, "age": student.age, "course": student.course, "phone": student.phone})
                print("File is saved.")