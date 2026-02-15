from manager.course_manager import CourseManager
from models.course import Course
from models.student import Student


class StudentManager:
    def __init__(self):
        self.__list_of_students: list[Student] = []
        self.__course_manager: CourseManager = CourseManager()


    def create_student(self,student_id: int, name:str, age:int, gender: str, phone_number:str):
        self.__validate_id(student_id)
        student = Student(student_id = student_id, name=name, age=age, gender=gender, phone_number=phone_number)
        self.__list_of_students.append(student)

    def get_student_name_ny_id(self, student_id):
        for student in self.__list_of_students:
            if student.get_student_id() == student_id:
                return student.get_name()
        return None

    def remove_student(self, student_id):
        for student in self.__list_of_students:
            if student.get_student_id() == student_id:
                self.__list_of_students.remove(student)

    def get_all_students(self):
        return self.__list_of_students

    def get_student_manager(self):
        return self.__course_manager

    def get_student_by_id(self, student_id):
        for student in self.__list_of_students:
            if student.get_student_id() == student_id:
                return student
        raise ValueError("Student ID does not exist")

    def get_course_by_id(self, course_title):
        for course in self.__course_manager.get_all_courses():
            if course.get_title() == course_title:
                return course
        raise ValueError("Course not found")

    def enroll_student_to_course(self, student_id: int, course_id: str):
        student = self.get_student_by_id(student_id)
        course = self.get_course_by_id(course_id)
        student.enroll_course(course)


    def __validate_id(self, student_id: int):
        for student in self.__list_of_students:
            if student_id == student.get_student_id():
                raise ValueError("Student ID already exists")

