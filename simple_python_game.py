import random

random_number = []

for x in range(3) :
    random_number.append(random.randint(0,10))
    if x > 0 :
        for y in range(x) :
            if random_number[x] == random_number[y] :
                random_number[x] = random.randint(0,10)
                y=0
while 1 :

    input_from_user = []

    for x in range(3) :
        input_from_user.append(input("enter a 1 digit number ",))
        if len(input_from_user[x]) > 1 :
            print("input too big only first digit will be taken")
            input_from_user[x] = input_from_user[x][0]

    for x in range(3) :
        input_from_user[x] = int(input_from_user[x])

    match = 0
    statement = 'nope'

    for x in range(3) :
        for y in range(3) :
            if input_from_user[y] == random_number[x] :
                if x == y :
                    statement = 'match'
                    match += 1
                    break
                elif statement == 'match' :
                    break
                else :
                    statement = 'close'
    if match == 3 :
        print("horraaayyyyy ^^")
        break
    else :
        print(statement)
