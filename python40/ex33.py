def shop(d):

    fr = []

    for x in d:
        val = d[x]

        fr.append((val / 100) * x)

    gprice = sum([x for x in fr])
                 
    print(f"final price : {((gprice * (int(input("iva\n")) / 100)) + gprice)}\noriginal price : {gprice}")

shop({100:10})