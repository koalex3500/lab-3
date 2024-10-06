#!/usr/bin/env python3

#this will be my function that returns the list
def give_list():
 return [100, 200, 300, "six hundred"]
#this will be my function to return the first item in the list
def give_first_item():
 my_list = give_list()
 return str(my_list[0])
#this will be  the function that returns first and last items in the list
def give_first_and_last_item():
 my_list = give_list()
 return [my_list[0], my_list[-1]]
#this will be the function that will return the second and third item on the list
def give_second_and_third_item():
 my_list = give_list()
 return [my_list[1], my_list[2]]
