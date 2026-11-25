full_name = "elliott"
age = 14
gpa = 3.2
is_student = True
print (f"hello {full_name}")
print (f"you are {age} years old")
print (f"your gpa is {gpa}")
print (f"are you a student?: {is_student}")

if is_student:
    print("you are a student")
else:
    print("you are NOT a student")



friends = 5

friends = friends + 1

print(friends)

name = "elliott"
age = 14
gpa = 3.2
is_student = True

print(type(is_student))

gpa = int(gpa)


name = ""
age = 3.2
is_student = True

name = bool(name)

print(name)


name = input("Enter your name: ")
age = input("Enter your age: ")

age = int(age)

age += 1

print(f"Hello {name}!")
print(f"you are {age} years old!")

age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")


if age < 18:
    print("You are a minor")


temp = -5
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

temp = 20
is_sunny = True
if temp >= 28 and is_sunny:
    print("it is HOT outside")
    print("it is SUNNY")
elif temp <= 0 and is_sunny:
    print("it is COLD outside")
    print("it is SUNNY")
elif temp > 28 > temp > 0 and is_sunny:
    print("it is WARM outside")
    print("it is SUNNY")
