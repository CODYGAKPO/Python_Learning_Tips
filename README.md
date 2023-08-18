# Python Learnings

## Variables
 - Containers that hold values that can vary (change)
 - They need to be given a name
   - ex. aidens_number, x, y and so on
 - Values in a variable can be modified
   - Once modified the variable will hold the new value. The old value will be erased.

Remember, variables hold values, and values can be of certain **types**. These are the python Data types, explained in the next section below.

## Data Types
### Scalar types 
 - Numeric types: Integers, Floats, Complex numbers
 - Boolean Types: the values True and False
 - String Types: A sequence of characters within quotes ('', "", """""")

#### Type Conversions
You can convert the data type of a variable by using the functions below

 - `int(x)`: This converts the variable `x` to an integer type
 - `float(x)`: This converts the variable `x` to a float type
 - `str(x)`: This converts the variable `x` to a string type

### Sequence Types
 - Lists
   - Created using the square brackets with values separated by ,
     - eg. [1, 3, 5, 7, 9]
   - Typically used to hold a homogeneous data type of values
 - Tuple
   - Created using the parentheses () with values separated by ,
     - eg, ('Aiden', 90)
   - Typically used to hold values of heterogenous data types
 - Range
   - Created by calling the range() function by passing the initial value, the ending value and optionally the step value: The STep value is the difference between each value in range
     - examples
       - range(10): 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
       - range(1, 10): 1, 2, 3, 4, 5, 6, 7, 8, 9
       - range(1, 10, 2): 1, 3, 5, 7, 9

You can use the `type()` function on a value or a variable to determine its data type.
Example
```
x = 10
print(type(x))

>>> <class 'int'>
```

## Operators
Different operators that can manipulate (change) values of different data types

 - Numeric types
   - Operators: +, -, /, *, **, %, <, >, <=, >=, and so on... 
 - Boolean
   - Operators: and, or
 - String
   - Operators: +

The most general operator that is used for all data types is the assignment operator which is =

This operator is used to assign a value to a variable as shown in the example below

```
# Assign the value 5 to the variable x
x = 5

# Add 10 to the value of the variable y and assign that result to the variable x
x = y + 10
```

#### Operator Precedence Rules
If an expression contains multiple operators, they will be evaluated as per the rules of operator precedence. This means that some operators will take precedence (will be evaluated before) others

The Order of Predence is as follows.

 1. Parentheses  ()
 1. Exponents  **
 1. Multiplication, Division, Remainder  *, /, %
 1. Addition, Subtraction  +, -

Expressions are always evaluated left to right.