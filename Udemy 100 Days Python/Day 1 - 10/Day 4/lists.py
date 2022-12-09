#data structure: a way of organizing and storing data in Python

fruits = ["Cherry", "Apple", "Pear"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina"
                     , "New Hampshire", "Virginia", "New York"]
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "Pencilvania"

states_of_america.append("Anthonyland")  # .append adds a single item to the end of a list
# more functions other than append on documentation on python
states_of_america.extend(["AnthonyIsland", "Jack Bauer Land"])  # adds a bunch of items to the end of list
print(states_of_america)
