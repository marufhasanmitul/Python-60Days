#return
def add(a, b):
    return a + b

result = add(10, 20)
print(result)

#Multiple return value
def calculation(a,b):
    return a+b,a-b,a*b

x,y,z = calculation(10,20)

print(x)
print(y)
print(z)

#==========Keyword Arguments====================

def student(name, age):
    print(name, age)

student(age=30, name="Maruf")

#যখন কতগুলো Argument আসবে জানা থাকে না।
def total(*numbers):
    print(sum(numbers))

total(10, 20)
total(10, 20, 30)
total(1, 2, 3, 4, 5)

def info(**data):
    print(data)

info(name="Maruf", age=30, city="Rangpur")