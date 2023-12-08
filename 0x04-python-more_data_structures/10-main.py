<<<<<<< HEAD
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score
=======
t_score = __import__('10-best_score').best_score
>>>>>>> c065d8bd456b6475a876a0882686e02710b80099

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
