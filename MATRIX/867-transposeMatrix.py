class Solution:
    def transpose(self, matrix):
        return zip(*matrix)

#     The zip(*matrix) line of code in Python is used to transpose a matrix, which means to convert
#     the rows of the matrix into columns, and columns into rows. It uses the zip function along with the * (unpacking)
#     operator to achieve this.
#
# Let's go through the example step by step using the given matrix matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]:
#
# Step 1: Understanding zip function
# The zip function is used to combine two or more iterables (e.g., lists) into tuples, where the first element from
# each iterable is paired together, the second element is paired together, and so on.
# For example, zip([1, 2, 3], [4, 5, 6]) will result in [(1, 4), (2, 5), (3, 6)].
#
# Step 2: Understanding * operator
# The * operator is used for unpacking a list or tuple. It allows elements from a list or tuple to be passed as separate
# positional arguments to a function. For example, *matrix is equivalent to passing matrix[0], matrix[1], matrix[2] as
# separate arguments.
#
# Step 3: Using zip(*matrix) to transpose the matrix
# In the given example, zip(*matrix) is used to transpose the matrix list of lists. When *matrix is passed to zip using
# the unpacking operator, it is equivalent to calling zip([1, 2, 3], [4, 5, 6], [7, 8, 9]), which means that each inner
# list in matrix is passed as a separate argument to zip.
#
# zip then pairs the elements from the first position of each inner list together, the second position together, and
# so on, creating tuples. In this case, the first position of each inner list corresponds to the first column of the
# original matrix, the second position corresponds to the second column, and so on.
#
# The resulting tuples represent the transposed matrix, where each tuple contains the elements from the same position
# across all inner lists. In this example, the resulting transposed matrix would be [(1, 4, 7), (2, 5, 8), (3, 6, 9)],
# which represents the columns of the original matrix as rows in the transposed matrix.


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    a = Solution()
    print(a.transpose(matrix))
