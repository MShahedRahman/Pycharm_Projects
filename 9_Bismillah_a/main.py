def fibonacci_sum(n):
    first_num = 0
    second_num = 1
    result = 0
    for i in range(0,n):
        result = first_num + second_num
        print(first_num , end='' )
        first_num = second_num
        second_num = result
        if (first_num>=100):
            break
    return result


n = int(input("Enter the limit: "))
x = fibonacci_sum(n)
print ('\nThe sum is: ', x)





