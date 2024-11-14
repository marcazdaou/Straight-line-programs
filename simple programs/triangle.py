import stdio
import sys

# Accept x (int), y (int), and z (int) as command-line arguments.
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Set expr to an expression which is True if each of x, y, and z is less than or equal to the sum
# of the other two, and False otherwise.
result = (x <= y + z) == 1 and (y <= x + z) == 1 and (z <= x + y) == 1

# Write expr to standard output.
stdio.writeln(result)
