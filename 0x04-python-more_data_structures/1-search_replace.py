<<<<<<< HEAD
#!/usr/bin/python3
def search_replace(my_list, search, replace):
=======
earch_replace(my_list, search, replace):
>>>>>>> c065d8bd456b6475a876a0882686e02710b80099
    new_list = list(map(lambda i: replace if i == search
                        else i, my_list))
    return new_list
