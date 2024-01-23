#ew casts

ap = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(str(ap[1]) + "\n" + str(ap[-1]) + "\n" + str(ap[7]) + "\n" + str(ap[0:2]) + "\n" + str(ap[2:-1]) + "\n" + str(ap[7] + ap[-1]) + "\n")

ap[8] = 30000
print(ap)

ap.append("pati interior")
ap.append(2.78)

print(str(ap) + "\n" + str(sum([x for idx, x in enumerate(ap) if idx % 2 != 0])))