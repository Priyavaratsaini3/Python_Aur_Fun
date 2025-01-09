def even_generator(limit):
    for i in range(2, limit + 2, 2):
        yield i

for num in even_generator(10):
    print(num)