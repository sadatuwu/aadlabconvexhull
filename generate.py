import random

#with test case: 

# with open('inputsteps.txt', 'w') as file:
#     t = 5
#     file.write(f"{t}\n")
#     ns = [20,50,100,200,500]
#     # n = random.randint(7,15)
#     for n in ns:
#         file.write(f'{n}\n')
#         for _ in range(n):
#             x = random.randint(-20,20)
#             y = random.randint(-20,20)
#             file.write(f'{x} {y}\n')



#without test case:

with open('input.txt', 'w') as file:

    n = random.randint(7,15)

    file.write(f'{n}\n')
    for _ in range(n):
        x = random.randint(-20,20)
        y = random.randint(-20,20)
        file.write(f'{x} {y}\n')