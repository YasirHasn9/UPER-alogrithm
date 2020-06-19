'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    idx = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[idx] = arr[i]
            idx += 1
        
    while idx < len(arr):
        arr[idx] = 0
        idx+=1

    return arr


print(moving_zeroes([0, -1, 1 ,0, 4, 5, 0]))


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")