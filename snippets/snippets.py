# For each of these exercises, run line by line in terminal unless specified

# SNIP1
# Do you think the following code will execute or will throw an error? Why?


x = 'iPhone'
y = x
y = 'Android'
print(y)


# SNIP2
# Do you notice a difference between the two lines of code? Why?


print(8.5/3)
print(8.5//3)


# SNIP3
# Do you think the following code will execute or will throw an error? Why?


a = ('London', 'Paris', 'Prague')
a.append('Rome')


# SNIP4
# Do you think the following code will execute or will throw an error? Why?


b = [10, 49, 190, 42, 50, 4, 28, 70]
print(b[:3])
print(b[3:])
print(b[3:8])


# SNIP5
# Now write the code below to a .py file in your terminal


def my_method(func):
    def inner():
        func()
        print("World!")
    return inner


def hello():
    print("Hello")


hello()
print("\n")
hello_world = my_method(hello)
hello_world()


# Execute your newly created .py file in terminal
# What can you observe about the behaviour of these functions? Why?
