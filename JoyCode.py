# sudo python -m pip install -U pip
# sudo python -m pip install -U matplotlib
# sudo apt-get install python-tk

# Import Modules
import sys
sys.path.append('.')

import Helpers.IO as io
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import emoji

# Import Packages
from Grade_K.TestCases import TestCasesK


def main():
    print(">>>> Joy Coding Main Function")

    while 1:
        print("Please choose the Grade of the student:")
        print("    k for Kindergarten")
        print("    [1-8] for Grade 1 to 8")
        grade = io.readChar()
        if grade in ['k', 'K']:
            break
        else:
            print("Only k is currently supported")
            continue

    k = TestCasesK()
    object_methods = [method_name for method_name in dir(k)                     if callable(getattr(k, method_name))]
    object_methods.remove('__init__')

    print("Please specify how many tests you want try:")
    testcnt = io.readInt()

    RandomMethodList = []
    for i in range(testcnt):
       secure_random = random.SystemRandom()
       m = secure_random.choice(object_methods)
       RandomMethodList.append(m)
       object_methods.remove(m)

    # recursively call all the test cases
    for name in RandomMethodList:
        getattr(k, name)()

if __name__ == '__main__':
    main()
