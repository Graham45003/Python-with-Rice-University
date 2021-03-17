print(list(range(0,5)))
print(range(0,5))
print(list(range(0,4,1)))
print(list(range(0,5,1)))

my_list=["This","course","is", "great","maybe"]
len(my_list)
print(my_list[3])

print(my_list[0 : len(my_list) // 2])
print(my_list[len(my_list) // 2 : len(my_list)])

init_list = list(range(1,5))
print (init_list)
final_list = init_list * 2
print (final_list)

test_string = "xxx" + " " * 2 + "xxx"
split_list = test_string.split(" ")
print(len(split_list))

def strange_sum(numbers):
    count = 0
    for num in numbers:
        if num % 3 != 0:
            count += num
    return count

print(strange_sum([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
print(strange_sum(list(range(123)) + list(range(77))))