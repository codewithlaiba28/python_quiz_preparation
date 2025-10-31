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

my_list_1: int = [1, 2, 3, "Java", 3.14, True]
my_list: list = [1, 2, 3, "Python", 3.14, 3+2j]

print(type(my_list_1), " my_list_1 = ", my_list_1)  
print(type(my_list), " my_list   =  " + str(my_list)) # we will look into type casting in classes ahead