import stdio
import sys

# accepts n1 (int), n2 (int), and p (float) as command-line arguments
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])
q = 1 - p
#  writes the probabilities p1 and p2 to standard output

p1 = (1 - (p / q) ** n2) / (1 - (p / q) ** (n1 + n2))
p2 = (1 - (q / p) ** n1) / (1 - (q / p) ** (n1 + n2))

# Compute and write the values of p1 and p2, separated by a space
stdio.write(p1)
stdio.write(" ")
stdio.writeln(p2)
