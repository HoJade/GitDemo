it = 4

while it > 1:
    if it != 3:
        print(it)
    it = it - 1

print('while loop execution is done')

print('**********')

it = 10

while it > 1:
    if it == 9:
        it = it - 1
        continue    # continue --> end the current iteration and start the next iteration

    if it == 3:
        break       # break --> terminate the (while) loop iteration

    print(it)
    it = it - 1

print('while loop execution is done')
