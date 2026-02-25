class ReportManager:

    def __init__(self, student_manager, enrollment_manager):
        self.student_manager = student_manager
        self.enrollment_manager = enrollment_manager


    def get_student_courses(self, student_id: int):
        return self.enrollment_manager.get_all_enrolled_course(student_id)


    def generate_student_report(self, student_id: int):

        student = self.student_manager.get_student_by_id(student_id)
        enrollments = self.enrollment_manager.get_all_enrollments()

        report_lines = ["=" * 60, f"STUDENT REPORT",
                        f"Name: {student.get_name()} | ID: {student_id}",
                        "=" * 60,
                        f"{'Course Code':<15}{'Mid(30)':<10}{'Final(70)':<12}{'Total':<8}{'Grade':<8}",
                        "-" * 60]

        for enrollment in enrollments:
            if enrollment.get_student_id() == student_id:
                mid = enrollment.get_mid_semester()
                final = enrollment.get_final_exam_score()
                total = enrollment.get_student_total_score()
                grade = self.__calculate_grade(total)

                report_lines.append(
                    f"{enrollment.get_course_title():<15}"
                    f"{mid:<10}"
                    f"{final:<12}"
                    f"{total:<8}"
                    f"{grade:<8}"
                )

        report_lines.append("=" * 60)

        return "\n".join(report_lines)


    def __calculate_grade(self, score: float):
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 45:
            return "D"
        elif score >= 40:
            return "E"
        return "F"