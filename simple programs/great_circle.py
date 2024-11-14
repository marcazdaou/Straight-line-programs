import math
import stdio
import sys

#  accepts x1 (float), y1 (float), x2 (float), and y2 (float) as command-line argument
x1 = math.radians(float(sys.argv[1]))
y1 = math.radians(float(sys.argv[2]))
x2 = math.radians(float(sys.argv[3]))
y2 = math.radians(float(sys.argv[4]))
f = 6359.83
# writes to standard output the great-circle distance d (in km) between them

d = f * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

# Compute and write the value of great-circle distance d.
stdio.writeln(d)
