from hpnm import hpapply
from prime import isPrime
import timeit

cnt = 0
l = list(range(1,10))

# def selcted4(l4):
# 	def isValid(l4, l5):
# 		global cnt
# 		if not isPrime(l4[0] * 100 + l4[1] * 10 + l5[0]): return False
# 		if not isPrime(l4[2] * 100 + l4[3] * 10 + l5[1]): return False
# 		if not isPrime(l5[4] * 100 + l5[3] * 10 + l5[2]): return False
# 		if not isPrime(l4[0] * 100 + l4[2] * 10 + l5[4]): return False
# 		if not isPrime(l4[1] * 100 + l4[3] * 10 + l5[3]): return False
# 		if not isPrime(l5[0] * 100 + l5[1] * 10 + l5[2]): return False
# 		cnt += 1
# 		# print("{} {} {}\n{} {} {}\n{} {} {}\n".format(l4[0], l4[1], l5[0], l4[2], l4[3], l5[1], l5[4], l5[3], l5[2]))
# 	hpapply([1,3,7,9], 5, lambda l5: isValid(l4, l5))

# hpapply(list(range(1,10)), 4,  selcted4)
# print(cnt)

# print(timeit.timeit(lambda: hpapply(l, 4,  selcted4), number=1))

def generateLine1(line1):
	if isPrime(line1[0] * 100 + line1[1] * 10 + line1[2]):
		def generateLine2(line1, line2):
			if isPrime(line2[0] * 100 + line2[1] * 10 + line2[2]):
				def generateLine3(line1, line2, line3):
					if not isPrime(line3[0] * 100 + line3[1] * 10 + line3[2]): return
					if not isPrime(line1[0] * 100 + line2[0] * 10 + line3[0]): return
					if not isPrime(line1[1] * 100 + line2[1] * 10 + line3[1]): return
					if not isPrime(line1[2] * 100 + line2[2] * 10 + line3[2]): return
					if not isPrime(line1[0] * 100 + line2[1] * 10 + line3[2]): return
					if not isPrime(line1[2] * 100 + line2[1] * 10 + line3[0]): return
					# print("{}\n{}\n{}\n".format(line1, line2, line3))
					global cnt
					cnt += 1
				hpapply(l, 3, lambda line3: generateLine3(line1, line2, line3))
		hpapply(l, 3, lambda line2: generateLine2(line1, line2))	

print(timeit.timeit(lambda: hpapply(l, 3, generateLine1), number=1))
print(cnt)