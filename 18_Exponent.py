def raise_to_power(base_num, pow_num):
    result=1
    for index in range(pow_num):
        result=result * base_num
    return result

print(raise_to_power(3,78))

# We are taking base number and result number

number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0])