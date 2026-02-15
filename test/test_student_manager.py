from unittest import TestCase

from manager.course_manager import CourseManager
from manager.student_manager import StudentManager


class Test(TestCase):

    def setUp(self):
        self.student_manager = StudentManager()


    def test_student_manager_create_student(self):
        self.student_manager.create_student(student_id = 1,
                                            name="samuel",
                                            age= 30,
                                            gender="male",
                                            phone_number="09134589101")

    def test_student_has_unique_id(self):
        self.student_manager.create_student(student_id= 1,name="samuel", age= 30, gender="male", phone_number="09134589101")
        with self.assertRaises(ValueError):
            self.student_manager.create_student(student_id=1, name="samuel", age=30, gender="male",
                                                phone_number="09134589101")

    def test_student_age_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(student_id=1, name="samuel", age= 0, gender="male", phone_number="09134589101")

    def test_student_gender_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(student_id=1, name="samuel", age= 20, gender="yyy", phone_number="09134589101")

    def test_student_phone_number_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(student_id=1, name="samuel",age= 30, gender="male", phone_number="091345889101")

    def test_student_name_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(student_id=1, name="ayobuu 99ami", age= 30, gender="male", phone_number="09134589101")

    def test_get_student_by_id(self):
        self.student_manager.create_student(student_id=1, name="samuel", age= 30, gender="male", phone_number="09134589101")
        self.student_manager.create_student(student_id=2, name="ayobami", age= 17, gender="male", phone_number="09134589101")
        self.assertEqual("ayobami", self.student_manager.get_student_name_ny_id(student_id=2))

    def test_delete_student(self):
        self.student_manager.create_student(student_id=1, name="samuel", age=30, gender="male",
                                            phone_number="09134589101")
        self.student_manager.create_student(student_id=2, name="ayobami", age=17, gender="male",
                                            phone_number="09134589101")
        self.student_manager.remove_student(2)
        self.assertEqual(None, self.student_manager.get_student_name_ny_id(student_id=2))


   