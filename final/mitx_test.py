from code_exam5 import *

courses = ('6.01x','6.02x','6.00x')

mitx = edx(courses)

mitx.setGrade(80)
#
#print mitx.getGrade()

#print mitx.myCourses[0].courseName

for i in range(len(mitx.myCourses)):
    print mitx.myCourses[i].courseName, mitx.myCourses[i].grade 
#print mitx