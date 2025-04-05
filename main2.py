# num1 = 5
# num2 = 5.0
# string = "Hello"
#
# print(type(num1))
# print(type(num2))
# print(type(string))

# intro_list = []
#
# for method in dir(intro_list):
#     print(method)
#
# data = "text"
#
# print(hasattr(data, "replace"))
# print(hasattr(data, "reverse"))
# print(hasattr(data, "startwith"))
# print(hasattr(data, "startwith", None))
# print(hasattr(data, "reverse", None))
#
# def first_func():
#     pass
#
# print(callable(data))
# print(callable(first_func))

class First:
    pass

class Second(First):
    pass

print(issubclass(First, Second))
print(issubclass(Second, First))

obj = Second()

print(isinstance(obj, Second))
print(isinstance(obj, First))