from manager.student_manager import StudentManager
from manager.enrollment_manager import EnrollmentManager
from manager.report_manager import ReportManager
from models.gender import Gender


def main():

    student_manager = StudentManager()
    course_manager = student_manager.get_course_manager()
    enrollment_manager = EnrollmentManager(course_manager)
    report_manager = ReportManager(student_manager, enrollment_manager)

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Student Management")
        print("2. Course Management")
        print("3. Enrollment Management")
        print("4. Reports")
        print("0. Exit")

        choice = input("Select option: ")

        if choice == "1":
            student_menu(student_manager)

        elif choice == "2":
            course_menu(course_manager)

        elif choice == "3":
            enrollment_menu(enrollment_manager)

        elif choice == "4":
            report_menu(report_manager)

        elif choice == "0":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")


def student_menu(student_manager):

    while True:
        print("\n--- Student Menu ---")
        print("1. Create Student")
        print("2. Remove Student")
        print("3. View All Students")
        print("4. View Student By ID")
        print("0. Back")

        choice = input("Select option: ")

        try:
            if choice == "1":
                name = input("Name: ")
                age = int(input("Age: "))
                gender_input = input("Gender (MALE/FEMALE): ").upper()
                phone = input("Phone Number: ")

                gender = Gender[gender_input]
                student = student_manager.create_student(name, age, gender, phone)
                print(f"Student created with ID: {student.get_student_id()}")

            elif choice == "2":
                student_id = int(input("Student ID: "))
                student_manager.remove_student(student_id)
                print("Student removed.")

            elif choice == "3":
                students = student_manager.get_all_students()
                for student in students:
                    print(f"ID: {student.get_student_id()} | Name: {student.get_name()}")

            elif choice == "4":
                student_id = int(input("Student ID: "))
                student = student_manager.get_student_by_id(student_id)
                print(f"ID: {student.get_student_id()}")
                print(f"Name: {student.get_name()}")
                print(f"Age: {student.get_age()}")
                print(f"Gender: {student.get_gender()}")
                print(f"Phone: {student.get_phone_number()}")

            elif choice == "0":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")


def course_menu(course_manager):

    while True:
        print("\n--- Course Menu ---")
        print("1. Add Course")
        print("2. Remove Course")
        print("3. View All Courses")
        print("0. Back")

        choice = input("Select option: ")

        try:
            if choice == "1":
                code = input("Course Code: ")
                title = input("Course Title: ")
                course_manager.add_course(code, title)
                print("Course added.")

            elif choice == "2":
                code = input("Course Code: ")
                course_manager.remove_course(code)
                print("Course removed.")

            elif choice == "3":
                courses = course_manager.get_all_courses()
                for course in courses:
                    print(f"Code: {course.get_code()} | Title: {course.get_title()}")

            elif choice == "0":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")



def enrollment_menu(enrollment_manager):

    while True:
        print("\n--- Enrollment Menu ---")
        print("1. Enroll Student")
        print("2. Add Mid-Semester Score")
        print("3. Add Final Exam Score")
        print("0. Back")

        choice = input("Select option: ")

        try:

            match(choice):

                case "1":
                    student_id = int(input("Student ID: "))
                    course_code = input("Course Code: ")
                    enrollment_manager.enroll_student(student_id, course_code)
                    print("Enrollment successful.")

                case "2":
                    student_id = int(input("Student ID: "))
                    course_code = input("Course Code: ")
                    score = int(input("Mid Score (0-30): "))
                    enrollment_manager.add_student_mid_semester_score(student_id, course_code, score)
                    print("Mid score added.")

                case "3":
                    student_id = int(input("Student ID: "))
                    course_code = input("Course Code: ")
                    score = int(input("Final Score (0-70): "))
                    enrollment_manager.add_student_final_exam_score(student_id, course_code, score)
                    print("Final score added.")

                case "0" :
                    break
                case _:
                    print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")


def report_menu(report_manager):

    while True:
        print("\n--- Report Menu ---")
        print("1. View Student Report")
        print("0. Back")

        choice = input("Select option: ")

        try:
            if choice == "1":
                student_id = int(input("Student ID: "))
                report = report_manager.generate_student_report(student_id)
                print(report)

            elif choice == "0":
                break

            else:
                print("Invalid choice")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()