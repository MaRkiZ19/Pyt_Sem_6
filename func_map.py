def f(x):
    return (x**2)**(1/3)

our_list=list(range(30))
list_square_and_cube_root=list(map(f, our_list))

for i in range(len(our_list)):
    our_list[i]=f(our_list[i])

print(list_square_and_cube_root)
print(our_list)