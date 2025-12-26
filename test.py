import subprocess
import sys
import unittest

class TestStudentGrade(unittest.TestCase):

    def run_program(self, args):
        result = subprocess.run(
            [sys.executable, "student.py"] + args,
            capture_output=True,
            text=True
        )
        return result.stdout

    def test_grade_s(self):
        output = self.run_program(["Harsha", "BCA", "3", "95", "92", "90"])
        self.assertIn("Grade      : S", output)

    def test_grade_a(self):
        output = self.run_program(["Anu", "BCA", "2", "85", "82", "80"])
        self.assertIn("Grade      : A", output)

    def test_grade_b(self):
        output = self.run_program(["Ravi", "MCA", "4", "70", "68", "75"])
        self.assertIn("Grade      : B", output)

    def test_grade_c(self):
        output = self.run_program(["Meena", "CSE", "1", "55", "52", "58"])
        self.assertIn("Grade      : C", output)

    def test_grade_f(self):
        output = self.run_program(["Sita", "ECE", "6", "30", "35", "38"])
        self.assertIn("Grade      : F", output)


if __name__ == "__main__":
    unittest.main()
