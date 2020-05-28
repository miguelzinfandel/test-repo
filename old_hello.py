#
# A simple python Script
#
import math
import sys
from os import rename

import requests

print("Sys:", sys.version)
print("Exe:", sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)

name = input("Your name? ")
print("Hello, ", name)