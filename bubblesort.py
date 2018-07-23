# Bubble Sort

def bubbleSort(array):
	n = len(array)

	# Traverse through all array elements
	for i in range(n):

		# Last i elements are already in place
		for j in range(0, n-i-1):

			# traverse the array from 0 to n-i-1
			# Swap if the element found is greater
			# than the next element
			if array[j] > array[j+1] :
				array[j], array[j+1] = array[j+1], array[j]

# sample test
array = [90, 15, 25, 4, 22, -3, 90]

bubbleSort(array)

print ("This array is sorted using bubble sort:")
for i in range(len(array)):
	print ("%d" %array[i]), 



