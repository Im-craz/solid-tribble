import matplotlib.pyplot as plt

# Demo Graph - Two Lines
x_one = [2, 4, 5, 6]
y_one = [2, 3, 6, 7]

plt.plot(x_one, y_one, label = 'Line One')


x_two = [1, 2, 3, 4]
y_two = [1, 2, 4 ,4]

plt.plot(x_two, y_two, label = 'Line Two')


plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Two Lines')

plt.legend()


plt.show()


# Demo Graph - Customization
x = [2, 3, 4, 5]
y = [3, 4, 5, 6]

plt.plot(x, y, color='green', linestyle='dashed', linewidth=3, marketr='o', markerfacecolor='blue', markersize=12)

plt.xlim(1, 8)
plt.ylim(1, 8)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Customization')

plt.show()


# Demo Graph - Bar Chart
left = [1, 2, 3, 4, 5]
height = [10, 11, 23, 36, 4]

tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['blue', 'orange'])

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Demo Graph - Bar Chart')

plt.show()
