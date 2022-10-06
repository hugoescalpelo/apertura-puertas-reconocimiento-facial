# https://docs.python.org/3/howto/argparse.html#id1

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("i", help="Path to img")
parser.add_argument("j", help="Path to img database")
args = parser.parse_args()
answer = ("img path " + args.i + " db path " + args.j)
print (answer)