
c = {}

while (str( ui := input("name and age\n")) != "0"):

    na = list(ui.split())

    if na[0] not in c:
        c.update({na[0]:na[1]})
        continue

    print("contact " + na[0] + " was not added\n")

print("contacts\n" + str(c))