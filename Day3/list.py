list1 = [1,20,30,50]   #list is like array but it can have any data type in python

print(list1)

list1.append("Gurditta")   #append will add the same object in list
print(list1)

print(id(list1))
for item in list1:  #for loop to print list
    print(item)
    if item == "Gurditta":
        print(f"found{item}")
    else:
        print("not found")