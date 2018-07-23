#Selection Sort
import sys
Array = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(Array)):
	
	# Find the minimum element in remaining 
	# unsorted array
	min_idx = i
	for j in range(i+1, len(Array)):
		if Array[min_idx] > Array[j]:
			min_idx = j
			
	# Swap the found minimum element with 
	# the first element	 
	Array[i], Array[min_idx] = Array[min_idx], Array[i]

# Test code
print ("This sorted array used the Selection Algorithm")
for i in range(len(Array)):
	print("%d" %Array[i]), 
