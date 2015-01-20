import random
import itertools
import pprint

people =[

]

def chunker(itr, size):
	item = list(itertools.islice(itr, size))
	while item:
		yield item
		item = list(itertools.islice(itr, size))

if __name__ == '__main__':
	no_of_groups = 3
	random.shuffle(people)
	groups = [g for g in chunker(iter(people), len(people)/no_of_groups)]
	pprint.pprint(groups)