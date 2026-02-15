import re


class Course:

    def __init__(self, course_code, title):
        self.__validate_code(course_code)
        self.__valdate_title(title)
        self.__course_code = course_code
        self.__course_title = title

    def get_code(self):
        return self.__course_code

    def get_title(self):
        return self.__course_title

    def set_code(self, code):
        self.__course_code = code

    def set_title(self, title):
        self.__course_title = title

    def __validate_code(self, course_code: str):
        if not re.match("^[A-Za-z]{2,4}[0-9]{3}$", course_code):
            raise ValueError("Invalid course code")

    def __valdate_title(self, course_title: str):
        if not re.match("^[A-Za-z]{4,15}$", course_title):
            raise ValueError("Invalid course title")


