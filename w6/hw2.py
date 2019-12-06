from prime import isPrime
import timeit

cnt = 0

def recursive(now, digit):
	if isPrime(now):
		if digit == 9:
			print(now)
			global cnt
			cnt += 1
		else:
			for i in range(1, 10):
				new = now + i*(10**digit)
				recursive(new, digit + 1)

def run():
	for i in range(1, 10):
		recursive(i, 1)

print(timeit.timeit(run, number = 1))

print(cnt)