#! /usr/bin/env python3

if __name__ == '__main__':
	n = int(input("Enter n value(n>1): "))

	print("*****************************  for  *****************************")
	for i in range(1, n+1, 1):
		for j in range(1, n+1, 1):
			print(i, "*", j, "=", i * j)

	print("****************************  while  ****************************")
	i = 1
	while i < n+1:
		j = 1
		while j < n+1:
			print(i, "*", j, "=", i * j)
			j += 1
		i += 1

