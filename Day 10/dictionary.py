#dictionary
student={
    "name":"Maruf",
    "age":18,
    "city":"Rangpur"
}

print(student)
print(student["name"])
print(student["age"])

student["Country"]="Bangladesh"
print(student)
student["age"]=28
print(student)

for key,value in student.items():
    print(key, ":",value)

print("")


print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
print(student.pop("age"))
print(student.clear())

#========================================

my_info={
    "name":"Maruf",
    "age":18,
    "profession": "OT Assistant"
}

print(my_info["profession"])
my_info["salary"]=30000

for key, value in my_info.items():
    print(key, ":", value)

student = {
    "name": "Rahim",
    "roll": 101,
    "department": "Science",
    "result": "A+"
}

print("Name:", student["name"])
print("Roll:", student["roll"])
print("Department:", student["department"])
print("Result:", student["result"])