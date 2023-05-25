import colorama
import inspect
import sys

print(colorama. __name__)

print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
print(inspect.getmodule(colorama))

print(sys.executable)
print(sys.version)
print(sys.platform)