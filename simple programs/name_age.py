import stdio
import sys
# Accept name (str) and age (str) as command-line arguments.
name = str(sys.argv[1])
age = str(sys.argv[2])

# Write the message "name is age years old." to standard output.
stdio.write(sys.argv[1])
stdio.write(" is ")
stdio.write(sys.argv[2])
stdio.writeln(" years old.")
