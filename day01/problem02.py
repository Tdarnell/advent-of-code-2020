import numpy as np
infile = np.genfromtxt("day01/input.txt", dtype=int)
sum_array1 = np.array([infile + n for n in infile])
# Improvement 1: Prevent duplicating the array, instead make a 200x200 sum array
sum_array2 = np.array([sum_array1 + n for n in infile])
sums = infile[np.where(sum_array2 == 2020)[0]]
# Improvement 2: This assumes there are no duplicate values in the input array, this could easily not be the case! Need to account for these
answer = np.prod(np.unique(sums))
print(answer)