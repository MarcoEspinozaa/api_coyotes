# api_coyotes

## Forma de uso

Clonar el repositorio para trabajar en su entorno local.

`$ git clone https://github.com/MarcoEspinozaa/api_coyotes`

Una vez abierto nuestro proyecto, ejecutamos el archivo **gendata.py**,
este archivo generará todos los archivos .json que necesitamos cargar en nuestra base de datos.
Con los archivos .json creados, procedemos a cargarlos y poblar nuestra DB.
Ejecutamos:


 -` python manage.py loaddata ingredientes_data.json`
 -` python manage.py loaddata platos_data.json`
 -` python manage.py loaddata menu_data.json`
 -` python manage.py loaddata menusemana_data.json`
 -` python manage.py loaddata ingredientesPlato_data.json`


Una vez cargados todos los archivos procedemos ejecutar nuestro proyecto.
Ejecutamos runserver desde la carpeta donde se encuetra el archivo.

`$ python manage.py runserver`


________________________________________________________________________

## Uso de la API

Para ver el menú de la semana ingresamos al siguiente link:

`http://127.0.0.1:8000/api/menu/`

Si se quiere ver un plato en particular, solo hay que ingresar la siguiente ruta con el **id** del plato en particular.

`http://127.0.0.1:8000/api/menu/platos/<id_plato>`

Para ver y eliminar un ingrediente de algun plato, debemos ingresar a la ruta:

`http://127.0.0.1:8000/api/menu/platos/<id>/ingrediente/<id_ingrediente>`

Ocupar el botón **DELETE** para borrar de manera lógica cada ingredente deseado de su plato.
