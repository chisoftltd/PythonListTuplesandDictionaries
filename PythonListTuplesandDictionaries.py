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

# Simple List Operations
print(scores + names)
print(names[2:5])
print(scores * 3)
print("Chinwe" in names)

for x in names:
    print(x)

# Indexing, Slicing, and Matrices

print(names[2:])
print(names[-2])
print(names[4])

# Python List Functions

print(max(grades))
print(min(scores))
print(max(names))

# Python List Methods
print(names.append("Bonaventure"))
print(names)
print(grades.extend(scores))
print(scores.reverse())
print(scores)
print(grades)

# Creating a New Tuple
tupNames = ('Benjamin', 'Joy', 'Shepherd', 'Emmanuel', 'Mikael')
tupGrades = ('A','B', 'C', 'D', 'E', 'F')
tupScores = (78, 37, 48, 99, 89, "Enugu", "Lagos", "Aberdeen")

# Accessing Elements of a Tuples
print(tupGrades[0])
print(tupNames[3])
print(tupScores * 3)

# Trying to Modify a Tuple
# tupNames[0] = "Uchenna" # Error
print(tupNames)

for y in tupScores:
    print(y)

# Indexing, Slicing and Matrices in Tuples
print(tupGrades[4])
print(tupScores[-3])
print(tupNames[2:])


# Tuple Function
print(max(tupNames))
print(min(tupGrades))
print(len(tupScores))

# Creating in a Dictionary
periodOfDay = {
    1: "Morning",
    2: "Afternoon",
    3: "Evening",
    4: "Night"
}

print("It is " + periodOfDay[1] + " time for breakfast.")
print("It is " + periodOfDay[4] + " time for sleep.")

# Dictionary Functions in Python
print(str(periodOfDay))
print(len(periodOfDay))

# Dictionary Methods in Python
print(periodOfDay.items())
print(periodOfDay.keys())
print(periodOfDay.values())