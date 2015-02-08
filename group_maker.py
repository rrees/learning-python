import random
import itertools
import pprint

# Issues to fix with this program

# Groups should be of the largest equal size
# Any people left over should be spread across the groups
# I.e. no-one left in a small group or just by themselves

people =[

]

def chunker(itr, size):
	item = list(itertools.islice(itr, size))
	while item:
		yield item
		item = list(itertools.islice(itr, size))

if __name__ == '__main__':
	no_of_groups = 3 # needs to be calculated
	random.shuffle(people)
	groups = [g for g in chunker(iter(people), len(people)/no_of_groups)]
	pprint.pprint(groups)
