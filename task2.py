def convert_to_final_grade(assessment_marks, supplementary_mark=None):
    final_grade = ''
    total_mark = sum(assessment_marks)
    if total_mark >= 80:
        final_grade = 'HD'
    elif total_mark >= 70:
        final_grade = 'D'
    elif total_mark >= 60:
        final_grade = 'C'
    elif total_mark >= 50:
        final_grade = 'P'
    else:
        if supplementary_mark is not None and supplementary_mark >= 50:
            final_grade = 'SP'
        else:
            final_grade = 'F'
    return final_grade


def get_grade_point_value(final_grade):
    grade_point_value = 0
    if final_grade == 'HD':
        grade_point_value = 4.0
    elif final_grade == 'D':
        grade_point_value = 3.0
    elif final_grade == 'C':
        grade_point_value = 2.0
    elif final_grade == 'P':
        grade_point_value = 1.0
    elif final_grade == 'SP':
        grade_point_value = 0.5
    else:
        grade_point_value = 0
    return grade_point_value


def get_assessment_marks():
    marks = input(
        "Enter a student's assessment marks (separated by comma), type in letter N to finish:")
    while marks != 'N':
        marks = [int(mark) for mark in marks.split(',')]
        total_mark = sum(marks)
        if total_mark < 50:
            supplementary_mark = int(
                input("Enter the supplementary exam mark:"))
            marks.append(supplementary_mark)
        yield marks
        marks = input(
            "Enter a student's assessment marks (separated by comma), type in letter N to finish:")


def main():
    all_students_marks = []
    all_students_final_grades = []
    all_students_grade_point_values = []
    for assessment_marks in get_assessment_marks():
        final_grade = convert_to_final_grade(assessment_marks)
        all_students_final_grades.append(final_grade)
        grade_point_value = get_grade_point_value(final_grade)
        all_students_grade_point_values.append(grade_point_value)
        all_students_marks.append(assessment_marks)

    total_grade_point_value = sum(all_students_grade_point_values)
    average_grade_point_value = total_grade_point_value / \
        len(all_students_grade_point_values)
    print("Total grade point value:", total_grade_point_value)
    print("Average grade point value:", average_grade_point_value)


if _name_ == '_main_':
    main()
