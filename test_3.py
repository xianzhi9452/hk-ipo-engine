import numpy as np
total_gains = []
for iii in range(1000):
    total_gain = 0
    for i in range(35):
        a = np.random.randint(0, 100)
        b = np.random.randint(0, 100)
        c = np.random.randint(0, 100)
        if a < 20:
            total_gain += 30000
        if b < 20:
            total_gain += 3000
        if c < 10:
            total_gain += 6000
    total_gains.append(total_gain)
print(np.std(total_gains))
print(np.mean(total_gains))