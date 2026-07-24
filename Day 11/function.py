def hello():
    print("Hello Maruf")
hello()

def greet(name):
    print("Hello ",name)

greet("Maruf")
greet("Rahim")

#Function Multiple Parameter Pass
def add(a,b):
    return a+b
result = add(10,20)
print(result)

#return Function
def square(x):
    return x*x
result = square(5)
print(result)

#Default Parameter
def country(name="United States"):
    print(name)

country("Bangladesh")








