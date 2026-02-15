from unittest import TestCase

from manager import enrollment_manager
from manager.course_manager import CourseManager
from manager.enrollment_manager import EnrollmentManager



class Test(TestCase):
    def setUp(self):
        self.course_manager = CourseManager()
        self.enrollment_manager = EnrollmentManager(self.course_manager)
        self.student_manager = enrollment_manager.StudentManager()

    def test_add_courses(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.course_manager.add_course("ENG101", "ENGLISH")
        self.enrollment_manager.enroll_student(1,"MATH101")
        self.assertEqual(1, self.enrollment_manager.get_numbers_of_enrollment())

    def test_get_name_of_enrolled_student(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.course_manager.add_course("ENG101", "ENGLISH")
        self.enrollment_manager.enroll_student(1, "MATH101")
        self.assertTrue( self.enrollment_manager.is_student_enrolled(1,"MATH101"))


    def test_get_list_of_all_courses_enrolled_by_student(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.course_manager.add_course("ENG101", "ENGLISH")
        self.enrollment_manager.enroll_student(1, "MATH101")
        self.enrollment_manager.enroll_student(1, "ENG101")
        course_list = ["MATH101", "ENG101"]
        self.assertListEqual(course_list, self.enrollment_manager.get_all_enrolled_course(1))

    def test_student_cannot_have_duplicate_enrollment(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.course_manager.add_course("ENG101", "ENGLISH")
        self.enrollment_manager.enroll_student(1, "MATH101")
        with self.assertRaises(ValueError):
            self.enrollment_manager.enroll_student(1, "MATH101")

    def test_student_cannot_enroll_for_unavailable_course(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        with self.assertRaises(ValueError):
            self.enrollment_manager.enroll_student(1, "MATH101")

    def test_add_mid_exam_score_for_student(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.enrollment_manager.enroll_student(1, "MATH101")
        self.enrollment_manager.add_student_mid_semester_score(1,"MATH101", 30)
        enrolled_course =  self.enrollment_manager.get_enrolled_course(1,"MATH101")
        self.assertEqual(30, enrolled_course.get_mid_semester())

    def test_add_final_exam_score_for_student(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.enrollment_manager.enroll_student(1, "MATH101")
        self.enrollment_manager.add_student_mid_semester_score(1, "MATH101", 30)
        self.enrollment_manager.add_student_final_exam_score (1, "MATH101", 70)
        enrolled_course = self.enrollment_manager.get_enrolled_course(1, "MATH101")
        self.assertEqual(70, enrolled_course.get_final_exam_score())

    def test_get_total_score_is_correct(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.enrollment_manager.enroll_student(1, "MATH101")
        self.enrollment_manager.add_student_mid_semester_score(1, "MATH101", 30)
        self.enrollment_manager.add_student_final_exam_score(1, "MATH101", 70)
        enrolled_course = self.enrollment_manager.get_enrolled_course(1, "MATH101")
        self.assertEqual(100, enrolled_course.get_total_exam_score())


    def test_mid_semester_score_cannot_be_greater_than_30_greater_than_zero(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.enrollment_manager.enroll_student(1, "MATH101")
        with self.assertRaises(ValueError):
            self.enrollment_manager.add_student_mid_semester_score(1, "MATH101", -1)
        with self.assertRaises(ValueError):
            self.enrollment_manager.add_student_mid_semester_score(1, "MATH101", 31)


    def test_final_exam_score_cannot_be_greater_than_70_greater_than_zero(self):
        self.student_manager.create_student(1, "omosefunmi", 30, "male", "09072175891")
        self.student_manager.create_student(2, "samuel", 18, "male", "09072175891")
        self.course_manager.add_course("MATH101", "MATHEMATICS")
        self.enrollment_manager.enroll_student(1, "MATH101")
        with self.assertRaises(ValueError):
            self.enrollment_manager.add_student_final_exam_score(1, "MATH101", -1)
        with self.assertRaises(ValueError):
            self.enrollment_manager.add_student_final_exam_score(1, "MATH101", 71)


