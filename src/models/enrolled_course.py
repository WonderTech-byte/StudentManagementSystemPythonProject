from models.course import Course


class EnrolledCourse:
       def __init__(self, student_id, course_id):
           self.__student_id = student_id
           self.__course_id = course_id
           self.__mid_semester = 0
           self.__final_exam = 0
           self.__total_exam_score = 0



       def get_student_id(self):
          return self.__student_id

       def get_course_id(self):
          return self.__course_id

       def get_mid_semester(self):
           return self.__mid_semester

       def get_final_exam_score(self):
           return self.__final_exam


       def get_total_exam_score(self):
           return self.__mid_semester + self.__final_exam

       def set_mid_semester(self, mid_semester):
           self.__mid_semester = mid_semester

       def set_final_exam_score(self, final_exam_score):
           self.__final_exam = final_exam_score



