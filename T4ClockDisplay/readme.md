# Declaración de Tarea

## Integrantes:
Alejandro López Torres
Felipe Galán

## Tareas por integrante

Se hizo la tarea en conjunto con un estilo de programación en pares, principalmente en formato online, con discusiones al respecto presencialmente pero sin avances concretos.

Felipe Galán: Aportó en la creación de los tests que generaban mas coverage. Alejandro asistió en estos tests con ideas para generar mas cobertura. También aportó en la capacidad de matar a los mutantes que generaba la libreria mutatest. 

Alejandro López: Se encargó principalmente en los tests unitarios con la librería pynguin. Diseñando y probando los casos de prueba para los test smells. Asistió en las pruebas para matar mutantes.

Respecto a la cobertura de lineas, si bien coverage muestra algunos archivos no con el 100%, si se ve el detalle, se ve que cada línea está cubierta exceptuando en display_number. 
Por algún motivo que no pudimos detectar, se testea la función reset(), pero dice que no se cubre la linea de reset del valor. Lo anterior, a pesar del test en la linea 45 que en teoría se asegura de que pase por ese "statement".

