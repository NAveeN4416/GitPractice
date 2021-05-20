#Ticket 458 Issue

class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

# Output: <function Person.greet>
print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)

# Output: "This is a person class"
print(Person.__data__)

# Output: "This is a person class"
print(Person.__class__.__name__)

# Output: <function Person.greet>
print(Person.greet)


# Output: "This is a person class"
print(Person.__doc__)



# Output: "This is a person class"
print(Person.__data__)