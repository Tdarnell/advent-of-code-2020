import numpy as np
# import the data
infile = np.genfromtxt("day01/input.txt", dtype=int)
# produce an array of 2020-the input
sum_array1 = np.array([infile + n for n in infile])
search_arr = (sum_array1-2020)*-1
intersects = np.intersect1d(infile, search_arr)
# product of the intersects
prod = np.prod(intersects)
print("Answer: ", intersects, " which sum to ", np.sum(intersects), " and product of these is ", prod)