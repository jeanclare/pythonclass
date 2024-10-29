#list datastructure, ordered, index, mutable or changeable, A list is an ordered,
# mutable collection of items, which can be of any data type.
# Lists allow duplicate values.



fruits = ["Mangoes", "Bananas", "Oranges", "Pineapples"]
fruits[1] ="Watermelon"
num= [5,1,8,1, -3,2,0,15]

print(fruits)
print(f"I love eating {fruits[1]}")

for i in fruits:
    print(i)

    print(num)

#tuples datastructures, immutable, unchanged
#A tuple is an ordered, immutable collection of items. Like lists, tuples can contain
#elements of different data types but once created, their contents cannot be changed.

cars = ("Subaru","Mercedes", "Nissan", "Toyota")
print(cars)
print(f"I love {cars[2]} cars")

#set datastructures, unordered, not indexed
#A set is an unordered collection of unique elements.
# Sets do not allow duplicate values, and the elements are not indexed.

colors= {"yellow", "blue", "green", "white", "orange"}
print(colors)

#dictionaries datastructures, key value pair
#A dictionary is an unordered collection of key-value pairs.
# Keys are unique, and each key is associated with a value.

staff = {"name": "Erick", "age": 50, "salary": 300000}
print(staff)
print(staff ["name"])



# Example of a list
my_list = [10, 20, 30, "apple", "banana"]

# Access elements
print(my_list[0])  # Output: 10
print(my_list[3])  # Output: apple

# Modify elements
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30, "apple", "banana"]

# Add an element
my_list.append("cherry")
print(my_list)  # Output: [10, 25, 30, "apple", "banana", "cherry"]

# Remove an element
my_list.remove("banana")
print(my_list)  # Output: [10, 25, 30, "apple", "cherry"]


# Example of a tuple
my_tuple = (10, 20, 30, "apple", "banana")

# Access elements
print(my_tuple[1])  # Output: 20
print(my_tuple[-1]) # Output: banana

# Tuples are immutable, so you cannot modify them
# This will raise an error: my_tuple[1] = 25

# You can convert a tuple to a list if you need to modify it
my_list = list(my_tuple)
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30, "apple", "banana"]


# Example of a set
my_set = {10, 20, 30, "apple", "banana", 30}

# Print the set (duplicates will be removed)
print(my_set)  # Output: {10, 20, 'apple', 30, 'banana'}

# Add an element
my_set.add("cherry")
print(my_set)  # Output: {10, 20, 'apple', 'cherry', 30, 'banana'}

# Remove an element
my_set.remove(20)
print(my_set)  # Output: {10, 'apple', 'cherry', 30, 'banana'}

# Sets do not support indexing, so you cannot do something like my_set[0]


# Example of a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}

# Access values by keys
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 25

# Add a new key-value pair
my_dict["profession"] = "Engineer"
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}

# Modify a value
my_dict["age"] = 26
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# Remove a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'profession': 'Engineer'}
