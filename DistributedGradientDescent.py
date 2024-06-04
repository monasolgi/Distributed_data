import numpy as np
import matplotlib.pyplot as plt
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#size=2

def y_hat(x, theta1, theta2):
    return theta1 * x + theta2

theta1 = 1
theta2 = 0
learning_rate = 0.006
E_max = 30

# Create the complete dataset on the root process (rank 0)
if rank == 0:
    X = np.arange(0, 1, 0.01)
    Y = X + np.random.normal(0, 0.2, len(X))
    x = np.array_split(X, size)
    y = np.array_split(Y, size)
else:
    x=None
    y=None
    X = None
    Y = None

# Scatter data to ranks
x_local = comm.scatter(x, root=0)
# print(rank,x_local)
y_local = comm.scatter(y, root=0)
# print(rank,y_local)
# Initialize variables for convergence check
theta1_change = np.inf
theta2_change = np.inf
#
# # Broadcast initial theta1 and theta2 values
theta1 = comm.bcast(theta1, root=0)
theta2 = comm.bcast(theta2, root=0)
#

for i in range(20):
    theta1_grad = np.mean((-2 * (y_local - y_hat(x_local, theta1, theta2))) * x_local)
    theta2_grad = np.mean(-2 * (y_local - y_hat(x_local, theta1, theta2)))
    #     # Update theta1 and theta2
    theta1 -= learning_rate * theta1_grad
    theta2 -= learning_rate * theta2_grad
    # print(rank,theta2_grad)
#
#     # Synchronize the gradients among all workers
#     theta1 = comm.gather(theta1)
#     theta2 = comm.gather(theta2)
if rank == 0:
        # print(i,theta1)
    print(theta1,theta2)


# #
#     theta1_change = np.abs(theta1_grad).max()
#     theta2_change = np.abs(theta2_grad).max()
# #
# #     # Gather the final theta1 and theta2 values from all workers
#     theta1_all = comm.gather(theta1, root=0)
#     theta2_all = comm.gather(theta2, root=0)
#
#     print(rank,theta1_all)
# #
#     if rank == 0:
#         if np.max([theta1_change, theta2_change]) < 0.5:
#             break
# #
#
