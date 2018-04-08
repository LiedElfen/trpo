#!/usr/bin/env python3

from calc import calc_line

if __name__ == '__main__':
	line = input()
	res = calc_line(line)
	print("{} = {}".format(line, res))
