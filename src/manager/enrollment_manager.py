from manager.course_manager import CourseManager
from manager.student_manager import StudentManager
from models.enrolled_course import EnrolledCourse


class EnrollmentManager:
    def __init__(self, course_manager_object: CourseManager):
        self.course_manager = course_manager_object

        self.__list_of_students = StudentManager().get_all_students()
        self.__list_of_enrollment: list[EnrolledCourse] = []

    def enroll_student(self, student_id: int, course_code: str) -> None:
        self.__check_course_exist(course_code)
        self.__check_duplicate_enrollment(student_id, course_code)
        self.__list_of_enrollment.append(EnrolledCourse(student_id, course_code))


    def get_numbers_of_enrollment(self) -> int:
        return len(self.__list_of_enrollment)

    def is_student_enrolled(self, enrolled_id, course_id ) -> bool:
        for enrolled in self.__list_of_enrollment:
            if enrolled.get_student_id() == enrolled_id and enrolled.get_course_title() == course_id:
                return True
        return False

    def get_all_enrollments(self):
        return self.__list_of_enrollment

    def get_all_enrolled_course(self, student_id) -> list[str]:
        course_list = []
        for enrolled in self.__list_of_enrollment:
            if enrolled.get_student_id() == student_id:
                course_list.append(enrolled.get_course_title())
        return course_list

    def __get_all_student_id(self)->list[str]:
        list_of_students = []
        for enrolled in self.__list_of_enrollment:
            list_of_students.append(enrolled.get_student_id())
        return list_of_students

    def __get_all_course_code(self):
        list_of_course_titles = []
        for course in self.course_manager.get_all_courses():
            list_of_course_titles.append(course.get_code())
        return list_of_course_titles


    def __check_duplicate_enrollment(self, student_id, course_id):
        for enrollment in self.__list_of_enrollment:
            if enrollment.get_student_id() == student_id and enrollment.get_course_title()==course_id:
                raise ValueError(f"Course {course_id} already enrolled for student {student_id}")


    def __check_course_exist(self, course_title):
        if course_title not in self.__get_all_course_code():
            raise ValueError(f"Course {course_title} does not exist")


    def get_enrolled_course(self, student_id, course_id):
        for enrolled in self.__list_of_enrollment:
            if enrolled.get_student_id() == student_id and enrolled.get_course_title() == course_id:
                return enrolled
        raise ValueError(f"{course_id} Enrollment for {student_id} does not exist")

    def add_student_mid_semester_score(self, student_id, course_id, score ):
        self.__validate_score(score, 30)
        enrolled_course = self.get_enrolled_course(student_id, course_id)
        enrolled_course.set_mid_semester(score)

    def add_student_final_exam_score(self, student_id, course_id, final_exam_score):
        self.__validate_score(final_exam_score, 70)
        enrolled_course = self.get_enrolled_course(student_id, course_id)
        enrolled_course.set_final_exam_score(final_exam_score)

    def get_student_total_score(self, student_id, course_id):
        for enrolled in self.__list_of_enrollment:
            if enrolled.get_student_id() == student_id:
                return enrolled.get_final_exam_score()
        return None

    def __validate_score(self, score, max_score):
        if score < 0 or score > max_score:
            raise ValueError("Score must be between 0 and 100")
