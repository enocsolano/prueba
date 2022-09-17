# prueba

Tienes que instalar con el pip install los requerimientos que se encuntran en requirementes.txt
Eso es para que te funcione tanto mysql con python y pyside2

### BASE TODO
Aquí tienes que traer toda la información de una base de datos que tu crees en mysql con workbench
la base de datos tendrá una tabla llamda usuarioos con la siguiente información:
- codigo
- nombre
- apellido
- edad
- calificacion

Con el botón refrecar te tienes que traer toda la información de la base de datos de esa tabla usuarios


### BASE DINAMICA:
En esta fase tienes que hacer algo similar que en *BASE TODO*
en la tabla otra vez tienes que traerte mediante el código, su nombre del usuario, su apellido
su edad, su calificación, 

pero ahora en este caso ahora tienes que hacer operaciones entre columnas, en la nueva columna
con nombre *nombre completo* tienes que hacer una concatenación de resultados y colocarlos en nombre completo
esa concatenación es de nombre + apellido

En la siguiente columna *suma de calificación y edad*
tienes que hacer una operación de entre la edad + calificacion 

IDEA: puedes hacer las consultas independientementes y traerte cada consulta para cada columna 
e ir colocandola como se solicita el nombre de la columna. 


DOCUMENTACIÓN QT: 
- https://doc.qt.io/qt-6/qtablewidget.html
- https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QTableWidget.html
