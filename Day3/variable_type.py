a = -.20
b = .30

print(type(a))
print(type(b))
a = 20
b = 30
print(type(a))
print(type(b))

print(id(a))  #printing the address id to get the address
print(id(b))  #printing the address

print(id(a))
z = 200
print(id(z)) #z also pointing to same location of a, this is concept of mutable,  remember a,b,z are called object
#immutable value in place not change, mutable not change

#list is collection of different data type

l = [1,2,3,4]
id(l)
print(l)
print(type(l))   #its class/type list