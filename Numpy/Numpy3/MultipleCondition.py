import numpy as np

numbers = np.array([12,25,8,40,15,30])
result = numbers[(numbers >= 15) & (numbers <= 30)]

print('\n\t-->Multiple Condition<--\n')
print('Numbers : ',numbers)
print('Numbers >= 15 and <= 30 : \n',result)