import json
import random

platos = [
    {'Cazuela de Pollo':['papas','porotos verdes','cilantro','pollo','choclo','arroz','cebolla']}, 
    {'Cazuela de vacuno':['papas','porotos verdes','cilantro','pollo','choclo','arroz','cebolla']},
    {'Caldillo de Congrio':['cebolla','papas','zanahoria','pimenton','congrio']},
    {'Carbonada':['cebolla','papas','zanahoria','pimenton','arvejas','carne']},
    {'Chorillana':['carne','papas fritas','cebolla','huevo']},
    {'Empanada de Pino':['aceituna']},
    {'Pastel de Choclo':['carne','pollo','huevo','aceituna']},
    {'Porotos granados':['pirco']},
    {'Pollo con Arroz':[]},
    {'Humitas':['azucar','tomate']},
    {'Carne con Arroz':[]},
    {'Fideos con Salsa':['salsa bolognesa','queso']},
    {'Pancutras':['cebolla','papas','zanahoria','pimenton','arvejas','carne','masa']},
    {'Charquicán':['cebolla','papas','zanahoria','pimenton','arvejas','carne']},
    {'Bistec a lo pobre':['carne','papas fritas','huevo']},
    {'Lasagna':['carne','queso','salsa blanca','salsa bolognesa']},
    {'Ceviche':['pescado','mariscos','cebolla','pimenton','cilantro']},
    {'Ensalada Cesar':['lechuga','pollo','crutones','queso']}
    ]

dias_semana = ('Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo')
lista_platos = []
lista_ingredientes = []
lista_ingredientes2 = []

for item in platos:
    lista_platos.extend(item)

for i,item in enumerate(platos):
    lista_ingredientes += list(item.items())[0][1]
new_ingredientes = set(lista_ingredientes)

for i,item in enumerate(platos):
    lista_ingredientes2.append(list(item.items())[0])

#print(lista_ingredientes2)
#print(lista_platos)
#print(len(lista_comunas))
#for item in lista_ingredientes2:
#    print(item[0])

# Creando json para menú
menu_data = []
model = "api.menu"
contador = 1
for item in dias_semana:
    for i in range(1,4):
        menu = {"model":model, "pk":contador, "fields": {"name":f'menu {i}', "description":item, "plato_id":random.randrange(1, 18, 1)}}
        menu_data.append(menu)
        contador += 1

with open("menu_data.json","w") as outfile:
    outfile.write(json.dumps(menu_data))
    


# Creando json para ingredientes
ingredientes_data = []
model = "api.ingrediente"
for i,item in enumerate(new_ingredientes):
    elem = {"model":model, "pk":i+1, "fields": {"name":item}}
    ingredientes_data.append(elem)

with open("ingredientes_data.json","w") as outfile:
    outfile.write(json.dumps(ingredientes_data))


# Creando json para platos
platos_data = []
model = "api.plato"
for i,item in enumerate(lista_platos):
    elem = {"model":model, "pk":i+1, "fields": {"name":item}}
    platos_data.append(elem)

with open("platos_data.json","w") as outfile:
    outfile.write(json.dumps(platos_data))


# Creando json para menú semanal
menusemana_data = []
model = "api.menusemana"
contador = 1
for i,item in enumerate(dias_semana):
    for x in range(1,4):
        elem = {"model":model, "pk":contador, "fields": {"title":f'Dia {i+1}',"menu_id":contador}}
        menusemana_data.append(elem)
        contador += 1

with open("menusemana_data.json","w") as outfile:
    outfile.write(json.dumps(menusemana_data))


# Creando json tabla intermedia
ingredientesPlato_data = []
model = "api.plato_ingredientes"
contador = 1
for plato in platos_data:
    #print(plato)
    for item in lista_ingredientes2:
        if item[0] == plato['fields']['name']:
            #print(f' {plato["fields"]["name"]} es igual a {item[0]} ')
            for ingrediente in item[1]:
                for data in ingredientes_data:
                    if ingrediente == data["fields"]["name"]:
                        #print(f' {ingrediente} es igual a {data["fields"]["name"]} ')
                        elem = {"model":model, "pk":contador, "fields": {"plato_id":plato["pk"],"ingrediente_id":data["pk"]}}
                        ingredientesPlato_data.append(elem)
                        contador += 1

with open("ingredientesPlatos_data.json","w") as outfile:
    outfile.write(json.dumps(ingredientesPlato_data))



