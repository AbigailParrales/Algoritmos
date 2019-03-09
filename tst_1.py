def count_sets(arr,total):
	return rec(arr, total, len(arr) -1)
def rec(arr, total, i):
	if total ==0:
		return 1
	elif total <0:
		return 0
	elif i < 0 :
		return 0
	elif total < arr[i]:
		return rec(arr, total , i-1)
	else:
		return rec(arr, total-arr[i],i-1)+rec(arr, total, i-1)
def dp(arr,total,i,mem):
	key = str(total)+':'+str(i)
	if key in mem:
		return mem[key]
	if total ==0:
		return 1
	elif total < 0:
		return 0
	elif i<0:
		return 0
	elif total < arr[i]:
		to_return = dp(arr, total, i-1,mem)
	else:
		to_return = (dp(arr, total - arr[i], i-1,mem)+dp(arr, total, i-1,mem))
	mem[key] = to_return
	return to_return

def count_sets_dp(arr, total):
	mem = {}
	return dp(arr, total, len(arr)-1,mem)

if __name__ == '__main__':

	intSet = [2,4,6,10]
	currCnt = count_sets(intSet,16)
	print (currCnt)