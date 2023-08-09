# import module1
# import module1 as mod1
# import module1 import *
# import module1 import each individual function
# from module1 import addition as add, subtraction as sub

import sys
sys.path.append('/home/stephen_hu/hha_506_class9/modules')
import module1

output1 = module1.addition(5, 10)
output2 = module1.subtraction(5, 10)

print('Output 1: ', output1)
print('Output 2: ', output2)

print(f'Output 1: {output1}')
print(f'Output 2: {output2}')