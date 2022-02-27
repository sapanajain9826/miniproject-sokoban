def create_gen(moves_list):
    for my_key in moves_list:
        yield my_key


moves_list = (['l', 'r', 'u', 'd'])
sol = create_gen(moves_list)
flag = True
while flag:
    try:
        print(next(sol))
    except StopIteration:
        break


# for i in sol:
#     print(i)

# print(sol.__dict__)