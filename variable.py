# declare
student_name="Gaurav"
student_roll_no= 11;
student_height=5.8;
#type
print(type(student_name))
print(type(student_roll_no))
print(type(student_height))
#address
print("Current Address: ", id(student_roll_no))


#how variable stored in a memory location

#golbal/ local variable
counter=10
def increment_of_counter():
    counter+=1
    print(counter)
    
    print(counter)