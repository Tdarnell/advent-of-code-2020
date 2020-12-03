import numpy as np
infile = np.genfromtxt("day01/input.txt", dtype=int)
sum_array = np.array([infile + n for n in infile])
# Improvement 1: Prevent duplicating the array, instead make a 200x200 sum array
sums = infile[np.where(sum_array == 2020)[0]]
answer = np.prod(sums)
print(answer)