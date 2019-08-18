import multiprocessing as mp
# https://www.machinelearningplus.com/python/parallel-processing-python/

import numpy as np

np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()


def how_many_within(row, min, max):
    count = 0
    for i in row:
        if min <= i <= max:
            count = count + 1
    return count


# Running without paralleization
results = []
for row in data:
    results.append(how_many_within(row, min=4, max=8))

print(results[:10])

# Parallelizing using Pool.apply()
pool = mp.Pool(mp.cpu_count())
results = [pool.apply(how_many_within, args=(row, 4, 8)) for row in data]
pool.close()
print("With paralleizing\n", results[:10])


# Difference between apply and map is that map only allows one input argument
def how_many_within_one(row, min=4, max=8):
    count = 0
    for i in row:
        if min <= i <= max:
            count = count + 1
    return count


pool = mp.Pool(mp.cpu_count())
results1 = pool.map(how_many_within_one, [row for row in data])
pool.close()
print("Map\n", results[:10])
