 
import math


assOne,assTwo,assThree = [float(x) for x in input(" Enter a student’s assessment marks (separated by comma):").split(',')]
print( assOne, assTwo,assThree)

x=((assOne/100)*20)+((assTwo/100)*40)+((assThree/100)*40)
print("Lab exercise : = %.2f" % assOne)
print("Report : = %.2f" % assTwo)
print("Final examination : = %.2f" % assThree)
print("Your final mark is : = %.2f" % x)


if x >= 85:print("Grade :HD") 
elif x >= 85:print("Grade :D") 
elif x>=65:print("Grade :C") 
elif x>=50:print("Grade :P") 
elif x>=45:print("Grade :F") 
else :print("Grade :AF"),
