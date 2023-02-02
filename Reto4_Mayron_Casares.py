productos=["Samsung","Xiaomi","Motorola","Huawei","Alcatel"]
precios = [950,750,720,890,670]

def total_compra(telefonos, cantidades):
#Escribe tu código de la función
  total_compra = 0

  if len(telefonos)==len(cantidades): # SI LOS DOS TIENEN LA MISMA DIMENSIÓN, AVANZO

    for i in range(len(telefonos)):   # 0 1 2 3 
      for j in range(len(productos)): # 0 1 2 3 4
        if telefonos[i] == productos[j]:
          total_compra = total_compra + precios[j]*cantidades[i]
          break 
    return total_compra  
  else:
    return 'Error'

def descuento(telefonos,cupon,total):
  descuento = 0
  count = 0
  DESCUENTO = [100, 200]

  if cupon == "H5K986W":
    if 'Samsung' in telefonos or 'Motorola' in telefonos:
      for a in telefonos:
        if a == 'Samsung':
          count += 1
        if a == 'Motorola':
          count +=1
        if count == 2:
          descuento = total - DESCUENTO[1]
        else:
          if count == 1:
            descuento = total - DESCUENTO[0]

      return descuento

  else:
    return 'Cupón inválido'

#--------------test------------------------------

telefonos = ["Samsung","Huawei","Motorola","Alcatel"]
cantidades = [2,1,1]
cupon = "H5K9845"

total = total_compra(telefonos,cantidades)
print('total compra: ',total)
total_desc = descuento(telefonos,cupon,total)
print('descuento: ',total_desc)

