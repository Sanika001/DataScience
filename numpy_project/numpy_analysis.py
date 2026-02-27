import numpy as np

sales = np.random.randint(100, 500, size=(5,3))

print("Sales Data:\n", sales)

print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Maximum Sale:", np.max(sales))
print("Minimum Sale:", np.min(sales))



print("\nProduct Wise Total:", np.sum(sales, axis=0))

print("\nProduct Wise Total:", np.sum(sales, axis=0))
