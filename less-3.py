import requests
import inspect
import sys

class Human:
    pass

def first_func():
    pass

rq=requests
first=first_func
nick=Human

print(requests.__name__)
print(rq.__name__)
print(first.__name__)
print(first_func.__name__)
print(nick.__name__)
print(Human.__name__)


print(type(1))
print(type(1.2))
print(type(1==1))
print(type('lmskcmsk'))


my_dict={}
for method in dir(my_dict):
    print(method)


print(inspect.ismodule(requests))
print(inspect.isclass(requests))
print(inspect.isfunction(requests))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

print(sys.executable)
print(sys.version)
print(sys.platform)