from unittest import TestCase


from manager.student_manager import StudentManager
from models.gender import Gender


class TestStudentManager(TestCase):

    def setUp(self):
        self.student_manager = StudentManager()


    def test_student_manager_create_student(self):
        self.student_manager.create_student(
                                            name="samuel",
                                            age= 30,
                                            gender =Gender.MALE,
                                            phone_number="09134589101")

    def test_student_has_unique_id(self):
        self.student_manager.create_student(name="samuel", age= 30, gender =Gender.MALE, phone_number="09134589101")

    def test_student_age_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(name="samuel", age= 0, gender =Gender.MALE, phone_number="09134589101")


    def test_student_phone_number_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(name="samuel",age= 30,gender =Gender.MALE, phone_number="091345889101")

    def test_student_name_is_validated(self):
        with self.assertRaises(ValueError):
            self.student_manager.create_student(name="ayobuu 99ami", age= 30,gender =Gender.FEMALE, phone_number="09134589101")

    def test_get_student_by_id(self):
        self.student_manager.create_student( name="samuel", age= 30, gender =Gender.MALE, phone_number="09134589101")
        self.student_manager.create_student(name="ayobami", age= 17, gender =Gender.FEMALE, phone_number="09134589101")
        self.assertEqual("ayobami", self.student_manager.get_student_name_by_id(student_id=2))

    def test_delete_student(self):
        self.student_manager.create_student( name="samuel", age=30, gender =Gender.MALE,
                                            phone_number="09134589101")
        self.student_manager.create_student( name="ayobami", age=17, gender =Gender.MALE,
                                            phone_number="09134589101")
        self.student_manager.remove_student(2)
        with self.assertRaises(ValueError):
            self.assertEqual(None, self.student_manager.get_student_name_by_id(student_id=2))


   