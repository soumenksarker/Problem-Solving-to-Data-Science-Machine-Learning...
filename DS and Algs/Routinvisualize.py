import matplotlib.pyplot as plt
days= [1,2,3,4,5]

sleeping = [7,8,11,9,5]
eating = [1,2,3,4,5]
working =[14,14,7,6,7]
playing =[2,3,7,8,9]

plt.plot([],[],color = 'm', label='Sleeping',linewidth=5)
plt.plot([],[],color = 'c', label='Eating',linewidth=5)
plt.plot([],[],color = 'r', label='Working',linewidth=5)
plt.plot([],[],color = 'k', label='Playing',linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors = ['m', 'c', 'r','k'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
plt.legend()
plt.show()

