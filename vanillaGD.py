#1 Implement Vanilla Gradient Descent (Not parallel)

import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x**2

def gradient(x):
    return 2*x

Emax = 20
learning_rate = 0.1
epsilon = 0.01
starting_point = 3.5
x_list = []
x = starting_point

for i in range(Emax):
    x_new = x - learning_rate * gradient(x)
    x_list.append(x_new)
    if abs(x_new - x) < epsilon:
        break
    x = x_new

y = [f(x) for x in x_list]
print(x_list, y)

#we need to plot the y=x**2 with plt.plot,
# and we assume that we have 200 points ranging from -4 to 4

x=np.linspace(-4,4,200)
y=f(x)
plt.plot(x,y)
#after that we plot our points for the gradient by using scatter()
plt.scatter(x_list, [f(x) for x in x_list],c='red')

plt.show()
