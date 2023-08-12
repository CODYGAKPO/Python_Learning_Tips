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

print(list(aiden_range))
print(list(shawn_range))