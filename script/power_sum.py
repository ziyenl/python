# This is solution for the power sum problem
# https://www.hackerrank.com/challenges/the-power-sum/problem
# Algorithm
# Recusion is used by breaking down the problem into two subset:
# One lineage will maintain that the target value without inclusion of the 'discovered' possible base power exp value
# Second lineage will reduce the target value by the 'discovered' possible base power exp value

import math

def power_sum(target, base, exp):
   # happens when it reduces the target to 0
    if target == 0:
        return 1
    elif base <= 0 or target <=0:
        return 0
    else:
        return  power_sum(target, base-1, exp) + power_sum(target-pow(base, exp), base-1, exp)
        
if __name__ == '__main__':
    target = input()
    exp = input()
    target = int(target)
    exp = int(exp)
    print(power_sum(target,int(math.sqrt(target)), exp)) 
  
