#!/usr/bin/python3

user_name = input("Enter Name: ")
current_year = int(input("Enter Current Year: "))
birth_year = int(input("Enter Year of Birth: "))
age = str(current_year - birth_year)

print("Hello " + user_name + ", you are " + age + " years old! ")
