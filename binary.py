# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):

	# Check base case
	if r >= l:

		mid = l + (r - l)/2

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid
		
		# If element is smaller than mid, then it 
		# can only be present in left subarray
		elif arr[mid] > x:
			return binarySearch(arr, l, mid-1, x)

		# Else the element can only be present 
		# in right subarray
		else:
			return binarySearch(arr, mid+1, r, x)

	else:
		# Element is not present in the array
		return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
# the function will test to see if 10 is in the area and then produce a string stating what (if any) index value it is at.
x = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
	print "Element is present at index %d" % result
else:
	print "Element is not present in array"

#The result of this test would produce 'Element is present at index 3'