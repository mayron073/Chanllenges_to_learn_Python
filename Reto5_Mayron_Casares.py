ocupacion = [[False,False,False],
             [False,False,False],
             [False,False,False]]

puestos ={1:[0,0],2:[0,1],3:[0,2],
          4:[1,0],5:[1,1],6:[1,2],
          7:[2,0],8:[2,1],9:[2,2]  
          }

def validar(puesto, ocupacion):
    a = 0
    b = 0
    c = 0
    if puesto in puestos:
        side = list(puestos[puesto])
        for i in puestos[puesto]:
               a +=1
               if a == 1:
                  b = side[0]
               if a == 2:
                  c = side[1]
               if ocupacion[b][c] == False:
                   return 'Libre'
               else:
                   if ocupacion[b][c] == True:
                      return 'Ocupado'

def ocupar(puesto, ocupacion, validacion):
    a = 0
    b = 0
    c = 0
    if puesto in puestos:
        side = list(puestos[puesto])
        for i in puestos[puesto]:
            a +=1
            if a == 1:
                b = side[0]
            if a == 2:
                c = side[1]
            if ocupacion[b][c] == False:
                ocupacion[b][c] = True
                
        return ocupacion
    

def liberar(puesto, ocupacion, validacion):
    a = 0
    b = 0
    c = 0
    if puesto in puestos:
        side = list(puestos[puesto])
        for i in puestos[puesto]:
            a +=1
            if a == 1:
                b = side[0]
            if a == 2:
                c = side[1]
            if ocupacion[b][c] == True:
                ocupacion[b][c] = False
                
        return ocupacion


#-----------------------first test-----------------
print('\nprimer test\n')
validacion = validar(2,ocupacion) #   validar y ocupar
print(validacion)
ocupacion = ocupar(2,ocupacion,validacion)
print(ocupacion[0][1])
#-----------------------------------------
validacion = validar(2,ocupacion) #   intentar ocupar un luagr ocupado
print(validacion)
ocupacion = ocupar(2,ocupacion,validacion)
print(ocupacion[0][1])
#-------------------------------------------
validacion = validar(2,ocupacion)#Liberar
print(validacion)
ocupacion = liberar(2,ocupacion,validacion)
print(ocupacion[0][1])
#-------------------------------------------
print('\nsegundo test\n')
#------------second test---------------------
validacion = validar(9,ocupacion)
print(validacion)
ocupacion = ocupar(9,ocupacion,validacion)
print(ocupacion[2][2])
#-------------------------------------------
validacion = validar(9,ocupacion)
print(validacion)
ocupacion = ocupar(9,ocupacion,validacion)
print(ocupacion[2][2])
#-------------------------------------------
validacion = validar(9,ocupacion)
print(validacion)
ocupacion = liberar(9,ocupacion,validacion)
print(ocupacion[2][2])