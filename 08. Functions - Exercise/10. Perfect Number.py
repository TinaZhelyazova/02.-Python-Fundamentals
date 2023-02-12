def perfect_number(num):
    sum_of_perfect_num = 0
    for i in range(1, num+1):
        if num % i == 0:
            sum_of_perfect_num += i

        if (sum_of_perfect_num+num) // 2 == num:
            return True


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
