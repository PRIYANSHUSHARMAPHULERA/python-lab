my_list1 = [{},{},{}]
my_list2 = [{123,2345},{},{}]
print(all(not d for d in my_list1))
print(all(not d for d in my_list2))