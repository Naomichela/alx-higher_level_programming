<<<<<<< HEAD
#!/usr/bin/python3
def weight_average(my_list=None):
    if my_list is None:
        my_list = []
    if not my_list:
        return 0
    weighted_product = 0
    total_weight = 0

    for score, weight in my_list:
        weighted_product += score * weight
        total_weight += weight
    if total_weight == 0:
        weighted_average = 0
    else:
        weighted_average = weighted_product / total_weight
    return weighted_average
=======
ght_average = __import__('100-weight_average').weight_average

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
>>>>>>> c065d8bd456b6475a876a0882686e02710b80099
