import matplotlib.pyplot as plt
days= [1,2,3,4,5]

sleeping = [7,8,11,9,5]
eating = [1,2,3,4,5]
working =[14,14,7,6,7]
playing =[2,3,7,8,9]

slices =[7,2,2,13]
activities = ['sleeping', 'eating', 'working', 'playing']
cols = ['m','c','r','b']
plt.pie(slices, labels=activities, colors=cols,
        startangle=90, shadow=True, explode=(0,.1,0,0),
        autopct='%1.1f%%')
plt.title('Interesting graph')
plt.show()

