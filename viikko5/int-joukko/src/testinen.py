a_taulu = [1, 2, 3]
b_taulu = [2, 3, 4, 5]

leikkaus = filter(lambda x: x in b_taulu, a_taulu)
print(list(leikkaus))
