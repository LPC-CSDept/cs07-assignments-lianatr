import matplotlib.pyplot as plt
import numpy as np

labels = ['Bill', 'Jim','Joe']
math1 = [100,100,100]
english1 = [90,90,80]
physics1 = [90,80,90]
computer1 = [90,80,90]

x = np.arange(3)
width = 0.15

fig, ax = plt.subplots()
math = ax.bar(x-width*1.5, math1, width,label='math')
english = ax.bar(x-width*.5,english1, width,label='english')
physics = ax.bar(x+width*.5, physics1, width,label='physics')
computer = ax.bar(x+width*1.5, computer1, width,label='computer')

ax.set_title("Grouped Graph for Scores")
ax.set_xticks(x);ax.set_xticklabels(labels)
ax.legend( )

ax.bar_label(math)
ax.bar_label(english)
ax.bar_label(physics)
ax.bar_label(computer)

plt.show()