<<<<<<< HEAD
#!/usr/bin/python3
search_replace = __import__('1-search_replace').search_replace
=======
earch_replace = __import__('1-search_replace').search_replace
>>>>>>> c065d8bd456b6475a876a0882686e02710b80099

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
