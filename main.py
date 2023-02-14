print('Nombre: Francisco Javier Queme Dominguez Carnet: 1552023 Carrera: Ingenieria en informatica y sistemas Primer ciclo')

import os

mi_ubicacion = os.getcwd()
if os.path.exists("modulos"):
    print("La carpeta ya existe")
else:
    os.mkdir(mi_ubicacion + "\\modulos")
    archivo = open('./modulos/prueba.txt', 'w')
    archivo.write('Hola mundo')
    archivo.close()
