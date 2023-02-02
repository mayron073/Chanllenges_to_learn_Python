#  no puede imprimir las coordenadas de las antenas...

def sector(x, y):
#sector 1
    if (x < 5 and x > 2) and (y > 6 and y < 9):
        print("S1")
    if (x == 2) and (y < 9 and y > 6):
        print("S1")
    if (y == 9) and (x < 5 and x > 2):
        print("S1")
#sector 2
    if (x < 8 and x > 5) and (y > 6 and y < 9):
        print("S2")
    if (x == 8) and (y < 9 and y > 6):
        print("S2")
    if (y == 9) and (x < 8 and x > 5):
        print("S2")
#sector 3
    if (x < 5 and x > 2) and (y > 3 and y < 6):
        print("S3")
    if (x == 2) and (y < 6 and y > 3):
        print("S3")
    if (y == 3) and (x < 5 and x > 2):
        print("S3")
#sector 4    
    if (x < 8 and x > 5) and (y > 3 and y < 6):
        print("S4")
    if (x == 8) and (y < 6 and y > 3):
        print("S4")
    if (y == 3) and (x < 8 and x > 5):
        print("S4")
#entre sectores
    if (x == 5) and (y >= 7 and y <= 9):
        print("Deniska está entre el Sector 1 y 2")

    if (x == 5) and (y >= 3 and y <= 5):
        print("Deniska está entre el Sector 3 y 4")

    if (y == 6) and (x > 1 and x < 5):
        print("Deniska está entre el Sector 1 y 3")

    if (y == 6) and (x > 5 and x < 9):
        print("Deniska está entre el Sector 2 y 4")
#fuera de sectores
    if (x <= 10 and x >= 0) and (y < 3 and y >= 0):
        print("Deniska ha escapado")
    if (x <= 10 and x >= 0) and (y <= 10 and y > 9):
        print("Deniska ha escapado")
    if (x <= 1 and x >= 0) and (y <= 9 and y >= 3):
        print("Deniska ha escapado")
    if (x <= 10 and x > 8) and (y <= 9 and y >= 3):
        print("Deniska ha escapado")
    
    
#===================principal=======================
x = float(input("digite corrdenada x: "))
y= float(input("digite corrdenada y: "))

ubicacion = sector(x, y)

