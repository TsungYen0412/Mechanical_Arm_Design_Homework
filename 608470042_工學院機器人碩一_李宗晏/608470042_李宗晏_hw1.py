#! /usr/bin/env python3

"""
My code use numpy module for python3, so you must install numpy module first.

sudo apt-get install python3-dev
sudo apt-get install python3-pip
pip3 install numpy
"""
import numpy as np

if __name__ == '__main__':
	print("******************************  Q1  ******************************")
	math_pass = {"Tom", "John", "Mary", "Jimmy", "Sunny", "Amy"}
	english_pass = {"John", "Mary", "Tony", "Bob", "Pony", "Tom", "Alice"}

	print("List of passing Math but failing English:", math_pass - english_pass)
	print("List of failing Math but passing English:", english_pass - math_pass)
	print("List of passing Math and English:", math_pass & english_pass)
	print("student count in the class:", len(math_pass | english_pass))

	print("******************************  Q2  ******************************")
	grade_of_homework = {"Tom" : [80, 100, 90, 95], "John" : [100, 93, 75, 80]}

	print("Tom's average of grade:", np.mean(grade_of_homework["Tom"]))
	print("John's average of grade:", np.mean(grade_of_homework["John"]))

