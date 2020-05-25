# Python Dya 7 by ChisoftMedia

# Creating a list
names = ['Benjamin', 'Joy', 'Shepherd', 'Emmanuel', 'Mikael']
grades = ['A','B', 'C', 'D', 'E', 'F']
scores = [78, 37, 48, 99, 89]

print(names[0])
print(len(grades))
print(scores + names)
print(names[2:5])
print(scores * 3)

# Modifying a List

# Updating existing elements
names[len(names) - 1] = "Mikael"

print(names)

# Add two more names to the names list
names.append("Chinwe")
print(names)

# Remove some names from the list
names.append("Nnaedozie")
print(names)

names.remove("Nnaedozie")
print(names)