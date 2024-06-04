from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Ensure that there are exactly 10 MPI processes
if size != 10:
    if rank == 0:
        print("This program requires exactly 10 MPI processes.")
    MPI.Finalize()
    exit()

# Define the neighbors in the cyclic ring
prev_rank = (rank - 1) % size
next_rank = (rank + 1) % size

# Initialize the integer i
initial_value = 1
if rank == 0:
    i = initial_value
else:
    i = None

# Track the start time
start_time = time.time()

# Initial send from rank 0
if rank == 0:
    print(f"Rank {rank} starting with {initial_value}")
    comm.send(i, dest=next_rank)

# Infinite loop for the ring communication
while True:
    # Check if 5 minutes have passed
    if time.time() - start_time > 300:
        if rank == 0:
            print("Stopping execution after 5 minutes.")
        break

    # Receive the integer from the previous rank
    i = comm.recv(source=prev_rank)
    print(f"Rank {rank} received {i} from Rank {prev_rank}")

    # Wait for 1 second
    time.sleep(1)

    # Increment the integer
    i += 1

    # Reset the integer to 1 after reaching 10
    if i > 10:
        i = initial_value
        if rank == 0:
            print(f"Resetting to {initial_value}")

    # Send the integer to the next rank
    comm.send(i, dest=next_rank)

    # Print the integer to show the iteration
    if rank == 0:
        print(f"Rank {rank} passed {i} to Rank {next_rank}")

# Finalize MPI
MPI.Finalize()