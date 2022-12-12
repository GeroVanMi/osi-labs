import sys
import argparse

# Since python scripts are called by using `python <filename>`, the first argument will always be the file name
name = sys.argv[0]
# All others are the r
args = sys.argv[1:]
print(name)
print(args)


# The argparse library gives options to require and parse arguments easily
parser = argparse.ArgumentParser(prog="Args Example")
parser.add_argument('path')
parsed_args = parser.parse_args()

print(parsed_args)