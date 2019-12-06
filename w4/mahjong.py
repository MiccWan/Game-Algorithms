from json import dumps as json_dump

def cnm(n, m):
	r = 1
	m = min(m, n-m)
	for i in range(n-m+1, n+1):
		r *= i
	for i in range(1, m+1):
		r /= i
	return r

def cntLines(arr):
	l = len(arr)
	res = 0

	for i in range(l):
		
		# horizontal
		res += (sum(arr[i]) == l)
		
		# vertical
		res += (sum([line[i] for line in arr]) == l)

	# diagonal
	res += (sum([arr[j][j] for j in range(l)]) == l)
	res += (sum([arr[j][l-1-j] for j in range(l)]) == l)
	
	return res

def applySelections(data, m, callback):
    
    n = len(data)
    l = list(range(m))
    
    while True:

        callback([data[i] for i in l])
        f_found = False
        
        for i in reversed(range(m)):
            if l[i] < n - m + i:
                f_found = True
                break

        if not f_found:
            return

        l[i] = l[i] + 1
        for j in range(i+1, m):
            l[j] = l[i] + j - i

def useSelections(selected):
	global l
	arr = list()
	for i in range(l):
		arr.append([0] * l)
	for i in selected:
		arr[i//l][i%l] = 1

	lines = cntLines(arr)
	# if lines == 0:
	# 	print("\n".join(list(map(lambda x: str(x), arr))))
	# 	print(lines)

	res[lines] += 1


# params
l_list = list(range(2, 6))
c_list = [3,6,10,15]


for l, choose in zip(l_list, c_list):
	# l = 3
	# choose = 6

	print("For {}*{} and pick {}:".format(l, l, choose))
	n = l*l
	res = [0] * (2 * l + 2)

	applySelections(range(n), choose, useSelections)

	res_dict = {}
	avg = 0
	for key, val in enumerate(res):
		if val:
			res_dict[key] = val
			avg += key * val
	avg /= cnm(l*l, choose)


	print(json_dump(res_dict, indent=2))
	print("In avg: {} lines\n".format(avg))


# ==== Output ====
# For 2*2 and pick 3:
# {
#   "3": 4
# }
# In avg: 3.0 lines

# For 3*3 and pick 6:
# {
#   "0": 2,
#   "1": 20,
#   "2": 46,
#   "3": 16
# }
# In avg: 1.9047619047619047 lines

# For 4*4 and pick 10:
# {
#   "0": 1564,
#   "1": 3904,
#   "2": 2284,
#   "3": 256
# }
# In avg: 1.1538461538461537 lines

# For 5*5 and pick 15:
# {
#   "0": 1456572,
#   "1": 1430612,
#   "2": 358504,
#   "3": 22836,
#   "4": 236
# }
# In avg: 0.6782608695652174 lines