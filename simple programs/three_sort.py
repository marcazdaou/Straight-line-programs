import stdio
import sys

#  accepts x (int), y (int), and z (int) as command-line arguments
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Find the smallest value α and largest value ω using min() and max() functions
a = min(x, y, z)
w = max(x, y, z)
Sn = (x * y * z)//(w * a)

#
stdio.write(a)
stdio.write(" ")
stdio.write(Sn)
stdio.write(" ")
stdio.writeln(w)
