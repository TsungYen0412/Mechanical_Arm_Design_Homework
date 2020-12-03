#! /usr/bin/env python3

import numpy as np


class Student:
	def __init__(self, name="", gender="", grades=[]):	
		self.name = name
		self.gender = gender
		self.grades = grades


	def avg(self):
		return np.mean(self.grades)


	def add(self, grade):
		self.grades.append(grade)


	def fcount(self):
		fail_count = 0
		for grades in self.grades:
			if grades < 60:
				fail_count += 1
		return fail_count


	def top(self, student):
		max_average_grade = 0
		max_average_student = []
		for i in range(len(student)):
			average_grade = student[i].avg()
			print(student[i].name + "'s average_grade:" + str(average_grade))
			print(student[i].name + "'s fail counts:" + str(student[i].fcount()) + "\n")
			if average_grade > max_average_grade:
				max_average_grade = average_grade
				max_average_student = student[i].name
			elif average_grade == max_average_grade:
				max_average_student.append(student[i].name)
		return max_average_student


def main():
	"""	
	student1 = Student("Tom", "M", [80, 100, 90, 95])
	student2 = Student("John", "M", [100, 93, 75, 80])
	student3 = Student("Amy", "F", [74, 88, 94, 86])
	"""
	student_cnt = int(input("Enter the number of students(ex.9): "))
	student = []
	for i in range(student_cnt):
		student_name = input("Enter student[" + str(i) + "]\'s name(ex. Tom): ")
		student_gender = input("Enter student[" + str(i) + "]\'s gender(ex. M or F): ")
		student_grades = input("Enter student[" + str(i) + "]\'s grades(ex. 80 100 90 95): ")
		print("")
		student_grades = list(map(int,student_grades.split( )))
		student.append(Student(student_name, student_gender, student_grades))
	Class = Student()
	print("The max average of grade's student:", Class.top(student))


if __name__ == '__main__':
	main()

