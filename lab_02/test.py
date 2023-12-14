import os
import csv
from unittest.mock import patch
from task import *
import unittest
import io

class Testing(unittest.TestCase):
    def setUp(self):
        self.testFile = "testData.csv"
        self.testData = [
            {"name": "Denys", "age": "22", "course": "3", "phone": "380982281927"},
            {"name": "Dmytro", "age": "21", "course": "2", "phone": "380982218392"},
            {"name": "Ivan", "age": "22", "course": "3", "phone": "380508380180"},
            {"name": "Matviy", "age": "23", "course": "2", "phone": "380954146429"},
            {"name": "Pavlo", "age": "24", "course": "1", "phone": "380974104357"},
            {"name": "Vadim", "age": "22", "course": "5", "phone": "380975128898"},
            {"name": "Zakhar", "age": "19", "course": "4", "phone": "380710994998"}
        ]

    def tearDown(self):
        if os.path.exists(self.testFile):
            os.remove(self.testFile)
    
    def test_loadFile(self):
        with open(self.testFile, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "age", "course", "phone"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.testData)

        updatedList = loadFile(self.testFile)
        self.assertEqual(updatedList, self.testData)

    def test_saveFile(self):
        listOfStundent = self.testData
        saveFile(self.testFile, listOfStundent)
        self.assertTrue(os.path.exists(self.testFile))

    def test_printAllList(self):
        listOfStundent = self.testData
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            printAllList(listOfStundent)
            output = mock_stdout.getvalue()
            self.assertIn("Denys", output)
            self.assertIn("Ivan", output)
            self.assertIn("Vadim", output)
            self.assertIn("Zakhar", output)

    def test_addNewElement(self):
        listOfStundent = self.testData
        with patch('builtins.input', side_effect=["Sasshko", "21", "3", "380995040294"]):
            addNewElement(listOfStundent)
            self.assertEqual(len(listOfStundent), 8)

    def test_deleteElement(self):
        listOfStundent = self.testData
        with patch('builtins.input', return_value="Denys"):
            deleteElement(listOfStundent)
            self.assertEqual(len(listOfStundent), 6)

    def test_updateElement(self):
        listOfStundent = self.testData
        with patch('builtins.input', side_effect=["Denys", "Dmytro", "21", "2", "380982218392"]):
            updateElement(listOfStundent)
            self.assertEqual(listOfStundent[0]["name"], "Dmytro")

if __name__ == '__main__':
    unittest.main()