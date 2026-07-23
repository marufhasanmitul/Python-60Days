#Tuple হলো List-এর মতোই একটি Collection, তবে Tuple পরিবর্তন (Modify) করা যায় না। এটিকে Immutable বলা হয়।

fruits = ("apple", "banana", "cherry")

print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])

#৩. Tuple পরিবর্তন করা যায় না
#fruits = ("Apple", "Banana", "Mango")
#fruits[0] = "Orange"

print(len(fruits))


colors = ("Red", "Green", "Blue")

for color in colors:
    print(color)

numbers = (10, 20, 10, 30, 10)

print(numbers.count(30))
print(numbers.index(10))














