def determine_interim_grade(assessment1, assessment2, assessment3):
    weighting1 = 0.2
    weighting2 = 0.4
    weighting3 = 0.4
    final_mark = round(assessment1 * weighting1 + assessment2 * weighting2 + assessment3 * weighting3)
    
    if final_mark >= 85:
        return "HD"
    elif final_mark >= 75:
        return "D"
    elif final_mark >= 65:
        return "C"
    elif final_mark >= 50:
        return "P"
    else:
        return "F"

assessment1 = float(input("Enter mark for assessment 1: "))
assessment2 = float(input("Enter mark for assessment 2: "))
assessment3 = float(input("Enter mark for assessment 3: "))

grade = determine_interim_grade(assessment1, assessment2, assessment3)
print("Interim grade: ", grade)

