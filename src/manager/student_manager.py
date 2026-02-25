from manager.course_manager import CourseManager
from itertools import count
from models.gender import Gender
from models.student import Student


class StudentManager:

    def __init__(self):
        self._student_counter = count(1)
        self._list_of_students: list[Student] = []
        self._course_manager: CourseManager = CourseManager()

    def create_student(self, name: str, age: int, gender: Gender, phone_number: str):
        student = Student(name=name, age=age, gender=gender, phone_number=phone_number)

        student_id = next(self._student_counter)
        self.__validate_id(student_id)

        student.set_student_id(student_id)
        self._list_of_students.append(student)

        return student

    def get_student_name_by_id(self, student_id: int):
        student = self.get_student_by_id(student_id)
        return student.get_name()

    def remove_student(self, student_id: int):
        student = self.get_student_by_id(student_id)
        self._list_of_students.remove(student)

    def get_all_students(self):
        return self._list_of_students

    def get_course_manager(self):
        return self._course_manager

    def get_student_by_id(self, student_id: int):
        for student in self._list_of_students:
            if student.get_student_id() == student_id:
                return student
        raise ValueError("Student ID does not exist")

    def get_course_by_id(self, course_title: str):
        for course in self._course_manager.get_all_courses():
            if course.get_title() == course_title:
                return course
        raise ValueError("Course not found")

    def enroll_student_to_course(self, student_id: int, course_title: str):
        student = self.get_student_by_id(student_id)
        course = self.get_course_by_id(course_title)
        student.add_course(course)

    def __validate_id(self, student_id: int):
        for student in self._list_of_students:
            if student_id == student.get_student_id():
                raise ValueError("Student ID already exists")