from xml.dom import minidom
import random

def student_dom():

    persons = [
    ["Juan", "Pérez", "juan.perez@gmail.com", "12345678T"],
    ["María", "Gómez", "maria.gomez@gmail.com", "87654321Y"],
    ["Carlos", "Rodríguez", "carlos.rodriguez@gmail.com", "98765432J"],
    ["Ana", "Martínez", "ana.martinez@gmail.com", "34567890K"],
    ["Pedro", "Sánchez", "pedro.sanchez@gmail.com", "56789012L"]]

    doc = minidom.Document()
    
    doc.appendChild(root := doc.createElement("students"))

    for person in persons:
        
        student = doc.createElement("student")
        student.setAttribute("id", str(random.randrange(0, 1000000)))

        n = doc.createElement("name")
        n.appendChild(doc.createTextNode(person[0]))
        student.appendChild(n)

        s = doc.createElement("surname")
        s.appendChild(doc.createTextNode(person[1]))
        student.appendChild(s)

        e = doc.createElement("email")
        e.appendChild(doc.createTextNode(person[2]))
        student.appendChild(e)

        d = doc.createElement("dni")
        d.appendChild(doc.createTextNode(person[3]))
        student.appendChild(d)

        root.appendChild(student)

    with open("ex22.xml", "w", encoding="utf-8") as file:
        dpx = doc.toprettyxml(indent="  ")

        print(dpx)

        file.write(dpx)

student_dom()