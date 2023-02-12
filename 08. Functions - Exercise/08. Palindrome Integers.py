def palindrome_numbers(nums):
    for num in nums:
        num_as_str = str(num)
        reversed_num = "".join(reversed(num_as_str))
        if num == int(reversed_num):
            print("True")
        else:
            print("False")


numbers = [int(x) for x in input().split(", ")]
palindrome_numbers(numbers)

