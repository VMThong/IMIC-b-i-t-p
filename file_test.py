import math
from math import *
class Solution():
    def isMatch(self, s, p):
        if s==p:
            print(True)
        else:
            i=0
            while i < len(s):
                for j in range(0,len(p)):




