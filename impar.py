#!/bin/python

import errno
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 > 0:
        result = "Weird"
    elif n%2 == 0 and n >6 and n<=20:
        result = "Weird"
    elif n%2 == 0 and n >2 and n<5 or n >20 and n%2==0:
        result = "Not Weird"
    
    print(result)