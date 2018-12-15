def fivaa(N):
	tmp = N
	for i in range(N):
		print(str(tmp-1)*2 + str(tmp+1) * tmp)
		tmp -= 1

fivaa(5)
