# author: JHR 11/7/22

# creating list
list = ["yellow:", "white", "black", "maroon"]

# extending list
list.extend(["red", "blue", "orange"])
list.insert(7, "gold")

# inserting color at 3
list.insert(3, "bronze")

# cloning list
list2 = list[:]

# removing item from clone
list2.remove("red")

# printing 
print(list)
print(list2)