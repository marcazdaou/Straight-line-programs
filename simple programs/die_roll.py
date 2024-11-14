import stdio
import stdrandom
import sys

#  accepts n (int) as command-line argument
n = int(sys.argv[1])

#  writes to standard output the sum of the numbers rolled
r = stdrandom.uniformInt(1, n+1)
i = stdrandom.uniformInt(1, n+1)

# Write the sum of the numbers rolled
stdio.writeln(r + i)
