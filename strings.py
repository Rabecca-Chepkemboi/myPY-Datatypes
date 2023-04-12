# 1. Write a Python program that takes in a list of integers
#and returns the largest number in the list.

def large(list):
    x= list[0]       #declare a variable that will store the largest value and initialise it to the 1st value
    for a in list:   #loop through the element(iteration)
        if a>x:      #compare it with the variable that stores the smallest value
            x=a
    return x         #return the variable
        

list=[4, 7, 5, 1, 8, 6]
print(large(list))




# 2. Write a Python program that takes in a list of strings
#and returns the longest string in the list.

w = ["peas", "mango", "fig", "apple"]
long = max(w, key=len)                         #use the max()function to fing the largest string
print(long)                                    #len to identify the length of each element   




# 3. Write a Python program that takes in a string and returns a 
# dictionary where the keys are the characters in the string 
# and the values are the number of times each character appears in the string.

str = "akirachix"
my_dict = {}
for words in str:
    my_dict[words] = my_dict.get(words, 0)+1            #.get() returns the value of a specified key is present in the dict
print(my_dict)    



# 4. Write a Python program that takes in a list of numbers and returns a 
# new list with only the even numbers from the original list.

def even(num_y):
    for c in num_y:                                   #iterate trough your function
        if c % 2 == 0:                                #check for the remainder
            print(c, end=" ")
even([22, 3, 2, 15, 34, 23])            



# 5. Write a Python program that takes in a dictionary where the keys 
# are strings and the values are integers, and returns a new 
# dictionary where the keys are the same strings but the 
# values are the square of the original integers.

my_dict = {"apple": 2, "banana": 3, "orange": 4, "kiwi": 5, "grape": 6}
for x in range(2, 6):                                 #iterate through the dict
    my_dict[x]=x**2                     #multiply the values in the range by 2 to find the square
print(my_dict)    





                                #   TAKEAWAY KEYS INCLUDES
    # 1. We can use tuples as keys but they must contain only strings, integers or other tuples.

    # 2. In python it is possible to access a section of items from the list using a slicing operator.

    # 3. Python lists are mutable(changeable) and you can change them by assigning new values using (=) operator.
