from prime import isPrime

cnt = 0

for i in range(100, 1000):
	for j in range(10):
		n = i * 10000 + j * 1000 + int(str(i)[::-1])
		if isPrime(n):
			cnt += 1
			print(n)

print(cnt)