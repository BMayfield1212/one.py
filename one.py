
# Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of code
# has been defined as below.

def hello_name(user_name):
    """ Print hello_USERNAME!"""
    print("hello_USERNAME!")

# Question 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing. The first 
# line of code has been defined as below.
          
          
hello_name("USERNAME") 


def first_odds():
    """ print odd nunbers 1-100"""
    print("Odd numbers from 1-100")
    for first_odds in range (1,100,2):
        print (first_odds)
print(first_odds())

# Question 3. Please write a python function, max_num_in_list to return the max number of a given list. The first line of
# code has been defined as below.

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
     if a > max:
        max = a
    return max
print(max_num_in_list([1,2,3,4,5]))

# Question 4. Write a function to return if the given year is a leap year. A leap year is divisible by 4
# but not divisible by 100, unless it is also divisible by 400. The return should be Boolean type (True/False). The first
# line of code has been defined as below.

def is_leap_year(a_year):
    
  leap = False
    
  if (a_year % 4) == 0:
        if (a_year % 100) == 0:
            if (a_year % 400) == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
  else:
        leap = False
    
  return leap

a_year=(2023)
print(is_leap_year(a_year))



# Question 5. Write a function to check to see if all numbers in list are consecutive numbers. For example, [2.3.4.5.6.7] 
# are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean type. The first line of 
# code is defined as below.

def is_consecutive(a_list):
   return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list=[2,3,4,5,6,7]
print(is_consecutive(a_list))





