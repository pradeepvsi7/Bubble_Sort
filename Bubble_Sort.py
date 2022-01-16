def sel(arr):
	for i in range(len(arr)):
		min_pos = i # POsition of 2 
		for j in range(i,len(arr)): 
			if arr[j] < arr[min_pos]: #Other values in arr which is < 2
				min_pos = j  # CHanging the position by updating new
		arr[i],arr[min_pos] = arr[min_pos],arr[i]
		print(arr)
	return arr
lst = [2,4,2,1,-1,21,3,9]
print(lst)
print(sel(lst))

# def sel(arr):
# 	for i in range(len(arr)-1,0,-1):
# 		for j in range(i):
# 			if arr[j]>arr[j+1]:
# 				arr[j],arr[j+1] = arr[j+1],arr[j]
# 	return arr
# lst = [2,4,2,1,-1,21,3,9]
# print(sel(lst))