# 1. Numeric Types

# a. Integer (int)
num_int: int = 42
print(type(num_int)," num_int = ",num_int,)


# b. Floating-Point (float)
num_float: float = 3.14
print(type(num_float), " num_float = ", num_float) 


# c. Complex (complex)
# Numbers with a real and imaginary part.
num_complex: complex = 2 + 3j
print(type(num_complex), " num_complex = ", num_complex)


# Accessing Real and Imaginary Parts
z = 3 + 4j
print("Real Part:", z.real)   # Output: 3.0
print("Imaginary Part:", z.imag)  # Output: 4.0




# 2. Boolean (bool)

is_python_fun: bool = True #False

print(type(is_python_fun), " is_python_fun = ", is_python_fun)  



# 3. Sequence Types

# a. String (str)
text_double: str  = "Hello, Python!" # Strings with Double Quotes (")
text_single: str  = 'Hello, Python!' # Strings with Single Quotes (')
text_multi: str   = '''Hello, Python!''' # Multi-Line Strings with Triple Quotes (''' or """)
text_multi_1: str = """Hello, Python!""" # Multi-Line Strings with Triple Quotes (''' or """)

print(type(text_double), " text_double   = ", text_double)    
print(type(text_single), " text_single   = ", text_single)    
print(type(text_multi), " text_multi    = ", text_multi)      
print(type(text_multi_1), " text_multi_1  = ", text_multi_1) 



# b. List (list)
# Ordered collection of items, mutable (can be changed).
my_list_1: int = [1, 2, 3, "Java", 3.14, True]
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)  
print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead




# c. Tuple (tuple)
# Immutable ordered collection of items.
my_tuple: tuple = (1, 2, 3, "AI", 2.71, False, .3 , 3+2j )
print(type(my_tuple), " my_tuple = ", my_tuple )  
print(type(my_tuple), " my_tuple = "+ str(my_tuple) )  


# d. Range (range)
# Represents a sequence of numbers.


num_range: range = range(1, 10, 1) # range(start, stop, step)
print(type(num_range), " num_range = ", num_range.step)  #
     

for i in range(1, 10, 2): # we will study loops indepth in classes ahead
  print(i)
     

# example for range to create a list

list = [1,2,3,4,5,6,7,8,9]
for i in range(0, len(list), 2): # we will study loops indepth in classes ahead
  print("Index:", i, "Value:", list[i])



# 4. Set Types
# items are unordered, unindexed, and do not allow duplicate values.the set itself is mutable.


# a. Set (set)


# Mutable, unordered, and contains unique values.
my_set: set = {1, 2, 33, 4, 4, 5}
print(type(my_set), "my_set = ", my_set)  



# b. Frozen Set (frozenset)

# Immutable version of a set.

frozen_set = frozenset([11, 2, 3, 4, 4, 5])
#frozen_set = frozenset(my_set)
print(type(frozen_set), " frozen_set = ", frozen_set) 