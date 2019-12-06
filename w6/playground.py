import timeit
from timeit import default_timer as timer

from cnmRec import applyRecSelections
from cphgen import cnm


start = timer()

for i in range(20):
	applyRecSelections(10,4,print)

t1 = timer() - start

start = timer()

for i in range(20):
	for i in cnm(10,4):
		print(i)

t2 = timer() - start



print(t1)
print(t2)