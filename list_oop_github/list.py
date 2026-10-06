student = ["Ibrahim", "Kelvin", "Shuaib"]
print(student)

# Accessing items in list by their index
print(f"My best friend is {student[0]}")
print(f"My best friend is {student[1]}")
print(f"My best friend is {student[2]}")

# get the index of an item in a list
print(student.index("Ibrahim"))
print(student.index("Kelvin"))

# know the number of item in the list
print(f"The total items in the list is: {len(student)}")

# Add items to a list
student.append("Marian")
print(student)
student += ["Kadiatu", "John", "Bintu"]

print(student)
student.insert(3, "Zara")
print(student)

# Extend a list
fruits= ["Apple", "Banana", "Mango"]

student.extend(fruits)
print(student)

# Removing from a list
fruits.remove("Mango")
print(fruits)

student.pop()
student.pop()
student.pop()
thirdItem = student.pop()
print(student)
print(thirdItem)






