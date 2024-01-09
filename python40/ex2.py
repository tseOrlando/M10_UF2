
eur = int(input("introduce cantidad de euros\n"))
iva = int(input("introduce cantidad de iva\n"))

print("\neur -> " + str(eur) + "\n"
        "iva -> " + str(iva) + "\n"
                  + str((eur * iva) / 100))