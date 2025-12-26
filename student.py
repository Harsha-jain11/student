import sys

def main():
    name = sys.argv[1]
    department = sys.argv[2]
    semester = sys.argv[3]

    marks1 = int(sys.argv[4])
    marks2 = int(sys.argv[5])
    marks3 = int(sys.argv[6])

    average = (marks1 + marks2 + marks3) / 3

    if 90 <= average <= 100:
        grade = "S"
    elif 80 <= average <= 89:
        grade = "A"
    elif 65 <= average <= 79:
        grade = "B"
    elif 50 <= average <= 64:
        grade = "C"
    elif 40 <= average <= 49:
        grade = "D"
    else:
        grade = "F"

    print("===== STUDENT DETAILS =====")
    print("Name       :", name)
    print("Department :", department)
    print("Semester   :", semester)
    print("Average    :", average)
    print("Grade      :", grade)

if __name__ == "__main__":
    main()
