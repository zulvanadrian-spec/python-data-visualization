# Create Data Daily Crowd in the Gym

import matplotlib.pyplot as plt

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
crowd= [66, 78, 59, 67, 49, 90, 78]

plt.plot(days, crowd, label='Crowd')

plt.title("Daily Crowd in the Gym")
plt.xlabel('Days')
plt.ylabel('Crowd')

plt.grid(True)
plt.legend()

plt.show()