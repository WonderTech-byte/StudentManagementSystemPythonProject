
from models.course import Course


class CourseManager:
    def __init__(self):
        self.__list_of_courses: list[Course] = []

    def add_course(self, course_code: str, course_title: str):
        self.__validate_course_code(course_code)
        self.__validate_course_title(course_title)
        self.__list_of_courses.append(Course(course_code, course_title))

    def test(self):
        self.add_course("MATH101", "Mathematics")


    def remove_course(self, course_code):
        for course in self.__list_of_courses:
            if course.get_code() == course_code:
                self.__list_of_courses.remove(course)


    def get_course_by_code(self, course_code):
        for course in self.__list_of_courses:
            if course.get_code() == course_code:
                return course
        return None


    def get_all_courses(self):
        return self.__list_of_courses

    def __validate_course_code(self, course_code: str):
        for course in self.__list_of_courses:
            if course.get_code() == course_code:
                raise ValueError("course code already exists")

    def __validate_course_title(self, course_title: str):
        for course in self.__list_of_courses:
            if course.get_title() == course_title:
                raise ValueError("course title already exists")


