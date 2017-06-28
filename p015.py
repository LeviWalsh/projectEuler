# How many lattice paths are there through a 20×20 grid?

def lattice_paths(gridSize):
	paths, i = 1, 0
	while i < gridSize:
		paths *= (2 * gridSize) - i
		paths //= i + 1
		i += 1
	return paths
print(lattice_paths(20))

# 137846528820



# I always thought this was the proper way to approach this type of problem. Still don't fully understand why it isn't working. Special thanks to Mr. McCullah for teaching me this approach and the one that worked back in 5th grade.
# # Create 20 rows
# row0 = [1 for x in range(0, 20)]
# row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18, row19 = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
# # Create the unpopulated grid
# grid = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11, row12, row13, row14, row15, row16, row17, row18, row19]

# # Populates the grid if it's already created to n size (works for anything 20 and lower)
# def lattice_paths(n):
# 	for i in range(1, n):
# 		for j in range(0, n):
# 			if 0 == j:
# 				grid[i].append(1)
# 			else:
# 				grid[i].append(grid[i - 1][j] + grid[i][j-1])
# 	return grid[-1][-1]

# print(lattice_paths(20))

# const int gridSize = 20;
# long paths = 1;
 
# for (int i = 0; i < gridSize; i++) {
#     paths *= (2 * gridSize) - i;
#     paths /= i + 1;
# }