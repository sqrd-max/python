# Declare variables with list and set types
my_list = [3, 1, 4, 1, 5]
my_set = {7, 5, 3, 9, 2}

# Iteratively create variables of different data types
my_tuple = (10, 20, 30, 5, 1, 8, 3, 2)
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Examples of manipulations with my_list and my_set

# Add an element to the list
my_list.append(9)
print("After adding:", my_list)

# Remove an element from the list (remove the first occurrence of 1)
my_list.remove(1)
print("After removing:", my_list)

# Add an element to the set
my_set.add(4)
print("After adding to set:", my_set)

# Remove an element from the set if it is a member
my_set.discard(7)
print("After discarding from set:", my_set)

# Sort the tuple
sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple:", sorted_tuple)

# Calculate the sum of tuple elements
sum_of_tuple = sum(sorted_tuple)
print("Sum of tuple elements:", sum_of_tuple)

# Create two lists
list_one = [1, 2, 3, 4, 5]
list_two = [4, 5, 6, 7, 8]

# Find common elements and return as a set
common_elements = set(list_one).intersection(set(list_two))
print("Common elements:", common_elements)

# Task 2
# a)
# dictionar_studenti = {'nume': 'Ana', 'varsta': 20, 'nota': 9.5}  # Dictionary
# print(dictionar_studenti)  # Print existing dictionary
# dictionar_studenti['gen'] = 'feminin'  # Add new pair to dictionary
# print(dictionar_studenti)  # Print new dictionary

# b)
# lista_intregi = [1, 2, 3, 4, 5]  # List
# lista_intregi.append(6)  # Append list with new element
# primul_element = lista_intregi[0]  # Extracting the first element of the list
# print(lista_intregi)  # Print new list
# print(primul_element)  # Print first element


# c)
# text = "Python este minunat!"
# text_nou = text + "Bunăăăăă!"
# lungime_text = len(text)  # Calculate the length of 'text'
# print(text, "a devenit", text_nou)
#
# # Print the length of 'text'. Note: Need to convert 'lungime_text' to string to concatenate
# print("lungimea textului meu este " + str(lungime_text))
#
# # print("lungimea textului meu este" + " " + lungime_text) # This is error
