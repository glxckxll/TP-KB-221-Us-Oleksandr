import os
from utils import Utils
from student import *
import unittest
from studentList import *


class Tests(unittest.TestCase):

    def test_Student(self):

        student = Student("Dmytro", "22", "2", "380982218392")
        self.assertEqual(student.name, "Dmytro")
        self.assertEqual(student.age, "22")
        self.assertEqual(student.course, "2")
        self.assertEqual(student.phone, "380982218392")

    def setUp(self):

        self.studentList = StudentList()
        self.student1 = Student("Denys", "22", "2", "380982281927")
        self.student2 = Student("Vadim", "22", "2", "380975128898")

    def test_addStudent(self):

        self.studentList.addStudent(self.student1)
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Denys")

        self.studentList.addStudent(self.student2)
        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[1].name, "Vadim")

    def test_deleteStudent(self):

        self.studentList.addStudent(self.student1)
        self.studentList.addStudent(self.student2)

        self.studentList.deleteStudent("Denys")
        self.assertEqual(len(self.studentList.students), 1)
        self.assertEqual(self.studentList.students[0].name, "Vadim")

        self.studentList.deleteStudent("Matviy")
        self.assertEqual(len(self.studentList.students), 1)

    def test_updateStudent(self):

        self.studentList.addStudent(self.student1)
        self.studentList.addStudent(self.student2)

        newStudent = Student("Denys", "22", "2", "380982281927")
        self.studentList.updateStudent("Denys", newStudent)

        self.assertEqual(len(self.studentList.students), 2)
        self.assertEqual(self.studentList.students[0].age, "22")
        self.assertEqual(self.studentList.students[0].phone, "380982281927")

        nonExistingStudent = Student("Matviy", "22", "2", "380954146429")
        self.studentList.updateStudent("Matviy", nonExistingStudent)

        self.assertEqual(len(self.studentList.students), 2)

    def test_loadFile(self):

        self.testFile = "unittests.csv"
        self.studentList = StudentList()
        with open(self.testFile, "w") as file:
            file.write("name,age,course,phone\nDmytro,22,2,380982218392")
        Utils.loadFile(self.testFile, self.studentList)
        self.assertEqual(len(self.studentList.students), 1)

    def test_saveFile(self):

        self.testFile = "unittests.csv"
        self.studentList = StudentList()
        student = Student("Dmytro", "22", "2", "380982218392")
        self.studentList.addStudent(student)
        Utils.saveFile(self.testFile, self.studentList)
        self.assertTrue(os.path.exists(self.testFile))

if __name__ == '__main__':
    unittest.main()