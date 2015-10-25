#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import argparse

XDG_CONF_DIR = os.environ.get('XDG_CONFIG_HOME') or os.environ.get('HOME')
CONF_DIR = os.path.join(XDG_CONF_DIR, 'AllTheDots')
DOT_LIST = os.path.join(CONF_DIR, 'savelist.txt')

def main():
	parser = argparse.ArgumentParser(description='Make a list of important stuff')
	parser.add_argument('paths', metavar='path', nargs='+', help='This file or directory is important stuff')
	args = parser.parse_args()
	abs_paths = [os.path.abspath(x) for x in args.paths]

	if not os.path.isdir(CONF_DIR):
		os.makedirs(CONF_DIR)

	with open(DOT_LIST, 'a+') as f:
		dotlist = [s.strip() for s in f.readlines()]
		for i in abs_paths:
			parents = [s for s in dotlist if i.startswith(s)]
			if len(parents) == 0:
				f.write(i+'\n')
				print '{dotpath} added to {dotlistfile}'.format(dotpath=i, dotlistfile=DOT_LIST)
			else:
				print '{dotlistfile} already contains {parents}'.format(dotlistfile=DOT_LIST, parents=' and '.join(parents))


if __name__ == '__main__':
	main()
