from unittest import TestCase

from manager.course_manager import CourseManager


class TestCourseManager(TestCase):
    def setUp(self):
        self.course_manager: CourseManager = CourseManager()

    def test_create_course(self):
        self.course_manager.add_course(course_code="MAT101", course_title ="MATHMATICS")

    def test_course_has_unique_code(self):
        self.course_manager.add_course(course_code="MAT101", course_title="MATHMATICS")
        with self.assertRaises(ValueError):
            self.course_manager.add_course(course_code="MAT101", course_title="ENGLISH")


    def test_course_has_unique_course_title(self):
        self.course_manager.add_course(course_code="ENG101", course_title="ENGLISH")
        with self.assertRaises(ValueError):
            self.course_manager.add_course(course_code="MAT111", course_title="ENGLISH")


    def test_remove_course(self):
        self.course_manager.add_course(course_code="ENG101", course_title="ENGLISH")
        self.course_manager.add_course(course_code="MAT101", course_title="MATHMATICS")
        self.course_manager.remove_course(course_code="MAT101")
        self.assertIsNone(self.course_manager.get_course_by_code(course_code="MAT101"))

    def test_course_code_must_be_letters_and_numbers_only(self):
        with self.assertRaises(ValueError):
            self.course_manager.add_course(course_code="MAT101++", course_title="MATHMATICS")

    def test_course_title_must_be_letters_only(self):
        with self.assertRaises(ValueError):
            self.course_manager.add_course(course_code="MAT101", course_title="MATHMAT222ICS")
