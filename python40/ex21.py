nl = [int (x) for x in list(input("10 nummers\n").split())]

print(nl)
print(str((sa := sum([x for x in nl])))+ "\n")
print(sa / len(nl))