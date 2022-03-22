import matplotlib.pyplot as plt
fig, ax = plt.subplots()
subjects = ['Math','English', 'Physics', 'Computer']
x = [1,2,3,4]
bill = [100,90,80,60]
mary = [90,80,70,100]

ax.bar(subjects, bill, label= 'Men')
ax.bar(subjects, mary, bottom=bill, label='Women')
ax.set_title("Stacked Graph for Scores")
ax.legend()

plt.show ()