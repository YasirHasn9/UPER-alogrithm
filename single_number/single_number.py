'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    sin = []
    for i in range(len(arr) - 1):
        if arr.count(arr[i]) == 1:
            sin.append(arr[i])

    return sin[0]


print("dd", single_number([1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]))


# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The odd-number-out is {single_number(arr)}")
