# ==================================
# Lab 5
# Script 5: Displaying College Majors
# ==================================

# Create a script that defines two variables for a student: 
# student_name and student_major. The student_major variable will 
# contain a code for the student’s major (e.g. ENG).

# Major Code    Name of Major      Department Office
# ---------------------------------------------------
# BIOL          Biology            Science Bldg, Room 310
# CSCI          Computer Science   Sheppard Hall, Room 314
# ENG           English            Kerr Hall, Room 201
# HIST          History            Kerr Hall, Room 114
# MKT           Marketing          Westly Hall, Room 310
# ---------------------------------------------------

# What should your program do if a major code is not included in the table? 
# Include an alternative to display <unknown> for the major name and nothing for location. 

# ---------------------------------------------------------------

# Final Script for Displaying College Majors for Students

# Ask for User Input
student_name = input('Enter your name: ')
student_major = (input('What is your major code?: ')).strip().upper()


# Loop for Looking up Major Name and Department Office

if student_major == 'BIOL':
    major_name = 'Biology'
    location ='Science Bldg, Room 310'
elif student_major == 'CSCI':
    major_name = 'Computer Science'
    location = 'Sheppard Hall, Room 314'
elif student_major == 'ENG':
    major_name = 'English'
    location = 'Kerr Hall, Room 201'
elif student_major == 'HIST':
    major_name = 'History'
    location = 'Kerr Hall, Room 114'
elif student_major == 'MKT':
    major_name = 'Marketing'
    location = 'Westly Hall, Room 310'
else : 
    major_name = '<unknown>'
    location = 'No location found'

print(f'Student Name: {student_name}')
print(f'Major Code: {student_major}')
print(f'Major Name: {major_name}')
print(f'Department Office: {location}')

# Output 1:
# Enter your name: Oscar
# What is your major code?: ENG
# Student Name: Oscar
# Major Code: ENG
# Major Name: English
# Department Office: Kerr Hall, Room 201

# Output 2:
# Enter your name: sharleen
# What is your major code?: CSI-100
# Student Name: sharleen
# Major Code: CSI-100
# Major Name: <unknown>
# Department Office: No location found
