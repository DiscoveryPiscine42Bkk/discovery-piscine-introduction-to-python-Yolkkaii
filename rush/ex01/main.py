from checkmate import checkmate

import sys

file = sys.argv[1:]

def main():
    for i in file:
        board = open(i).read()
        checkmate(board)

if __name__ == "__main__":
    main()