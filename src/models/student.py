import re
from ast import List

from models.course import Course
from models.enrolled_course import EnrolledCourse


class Student:
    def __init__(self, student_id ,name, age, gender, phone_number):
        self.__validate_student_name(name)
        self.__validate_phone_number(phone_number)
        self.__validate_gender(gender)
        self.__validate_age(age)
        self.__student_id = student_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__phone_number = phone_number
        self.__enrolled_courses: List[EnrolledCourse] = []


    def get_student_id(self):
        return self.__student_id

    def  get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_phone_number(self):
        return self.__phone_number

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_gender(self, gender):
        self.__gender = gender

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def enroll_course(self,enrolled_course: Course):
        self.__enrolled_courses.append( EnrolledCourse(enrolled_course))

    def __validate_age(self, age):
        if age < 16 or age > 50:
            raise ValueError("Age must be between 16 and 50")

    def __validate_gender(self, gender):
        if not re.fullmatch(r"(MALE|FEMALE)", gender, flags=re.IGNORECASE):
            raise ValueError("Gender must be either MALE or FEMALE")

    def __validate_phone_number(self, phone_number):
        if not re.fullmatch(r"^(090|091|081|080|070|071)\d{8}$", phone_number):
            raise ValueError("phone number must match correct pattern")

    def __validate_student_name(self, name):
        if not re.fullmatch(r"[A-Za-z]+$", name):
            raise ValueError("Student name must contain only letters")