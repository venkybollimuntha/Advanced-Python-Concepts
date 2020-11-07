print((lambda x: x + 1)(2))


add = lambda x,y,z=5: x + y + z +1
print(add(2,3))


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name("venky","bollimuntha"))


x = lambda x:(x % 2 and 'odd' or 'even')
print(x(3))

def squares():
    return lambda a,b: a*b

l = squares()
print(l(10,10))
