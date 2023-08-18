import exercise

# Scalar data types
#integer value type
aidens_number = 1

#this is a float value type
nikhils_number = 1.36

#these are boolean value types
aidens_bool = True
nikhils_bool = False

#this is a string valur type
ericas_string = """a nice mom"""
nikhils_string = "This is nikhil's string"


print("This is Aidens number", aidens_number)
print("This is Nikhils number", nikhils_number)

print('This statement is...', nikhils_bool)
print('This statement is...', aidens_bool)

print('Erica is',ericas_string)
print("this is nikhils_string", nikhils_string)

# Sequence Data types
# List value type
# You use it to store values that are of the same type: homogenous
meghas_list = [1,2,3,45,66,70]

# Tuple value type
# You use this to store values of different types (heterogeneous)
name_age = ('Aiden', 12)
ishwar_tuple = ('hi grandpa', 'how are you?')

# Range value type
# Convenient way to create a sequence that is a range of values
aiden_range = range(1, 11)
shawn_range = range(1, 11, 4)
  


print('The three numbers are...', meghas_list)

print(ishwar_tuple)
print("Name and Age: ", name_age)


# print(list(aiden_range))
# print(list(shawn_range))


# aiden_var = '345'
# print('Value of aiden_var: ', aiden_var, 'The Type of aiden_var: ', type(aiden_var))

# aiden_var = int(aiden_var)
# print('Value of aiden_var: ', aiden_var, 'The Type of aiden_var: ', type(aiden_var))

# aiden_var = float(aiden_var)
# print('Value of aiden_var: ', aiden_var, 'The Type of aiden_var: ', type(aiden_var))

# aiden_var = str(aiden_var)
# print('Value of aiden_var: ', aiden_var, 'The Type of aiden_var: ', type(aiden_var))

# result = aiden_var + 10
# print("The result of the operation of addint 10 to aiden_var is: ", result)


var_1 = 123
var_2 = 345

print('The type of var_1: ', type(var_1), " The type of var_2: ", type(var_2))
result = var_1 + var_2
print(result)

print(list(aiden_range))
print(list(shawn_range))
