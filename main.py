# import module1
# import module1 as mod1
# import module1 import *
# import module1 import each individual function
from module1 import addition as add, subtraction as sub

output1 = add(5, 10)
output2 = sub(5, 10)

print('Output 1: ', output1)
print('Output 2: ', output2)

print(f'Output 1: {output1}')
print(f'Output 2: {output2}')