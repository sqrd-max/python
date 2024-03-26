# 1. Declare variables
integer_variable = 42  # Integer value
float_variable = 3.14  # Floating-point value
text_variable = "hello"  # Short text value
multi_line_text = """This is a longer piece of text,
spanning several lines,
to demonstrate multi-line strings in Python."""  # Multi-line text value

# 2. Display the length of one of the text variables
print("Length of 'multi_line_text':", len(multi_line_text))

# 3. Convert text to uppercase
upper_text = text_variable.upper()
print("Uppercase text:", upper_text)

# 4. Extract and display a substring
substring = multi_line_text[10:25]
print("Extracted substring:", substring)

# 5. Request age input from the user and use it in an arithmetic calculation
user_input = input("Enter your age: ")
age = int(user_input)
age_in_five_years = age + 5
print("In 5 years, you will be " + str(age_in_five_years) + " years old.")


# 6. Create lists and display product information
number_list = [100, 200, 300]  # List of numbers
product_list = ["Apples", "Oranges", "Bananas"]  # List of strings representing product names

# Use format() method to construct and display product information
for i in range(3):
    print("The price of {0} is ${1}.".format(product_list[i], number_list[i]))

# Task 2
txt = "More results from text..."
substr = txt[4:12]  # Extract characters from 4 to 12
print(substr)  # Print extracted characters " results"
print(substr.strip())  # Removes whitespace characters from the beginning and end of a string
"""
output:  results
        results
"""

txt = "More results from text..."
print(txt.split())  # Splits a txt string into a list of substrings based on whitespace characters
"""
output:  ['More', 'results', 'from', 'text...']
"""
