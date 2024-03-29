# MCOC-Proyecto-2 entrega 4 (individual)
# INTRODUCCION:
En este proyecto se implementará y validará un modelo de simulación de transporte de
sedimentos en base a un método lagrangiano, es decir que sigue a cada partícula individualmente.
La validación se hará a nivel del comportamiento de una partícula y luego con el comportamiento
estadístico de cantidades crecientes de partículas. Además, se explorará cómo influyen las
decisiones de algoritmo de implementación, conocido como complejidad computacional, y
métodos de input-output (IO) en el rendimiento del programa.

# OBJETIVOS:
Diseñar un modelo que simule el transporte de partículas de sedimento en el fondo del agua.
Entender la influencia de la implementación de algoritmos computacionales, entre ellos
algoritmos de complejidad computacional y métodos (IO).
[Meta 3]: implementación del código para una partícula con perfil de velocidad

# RESULTADOS PARA UNA PARTÍCULA:

Para el estudio del comportamiento de una partícula transportada por un fluido se usaron los siguinetes datos y supuestos:
* La partícula transportada corresponde a una grano de arena
* La forma de la artícula es considerada como esférica 
* EL comportamiento se estudia mediante relaciones Euler-Lagrange

* Datos usados

    * diámetro de partícula = 1 mm
    * densidad de partícula = 155 kg/m^3
    * coeficiente Drag para partícula esférica = 0,47

El desplazamiento en x de la partícula según la velocidad con que se mueve se muestran el el siguiente gráfico, donde el eje "x" representa el desplazameinto y el eje "y" la velocidad en cierto instante 

![real p2](https://user-images.githubusercontent.com/53712876/65996866-a65a9300-e46e-11e9-945e-d2ca47f3125f.png)

# Discucion de resultados:
Caracteristicas del computador:
- Marca: HP
- Procesador: Intel(R) Core(TM) i3-31100M CPU @ 2.40GHz
- Memoria instalada (RAM): 4.00 GB (3,89 GB utilizable)
- Tipo de sistema: Sistema operativo de 64 bits, procesador x64
- Edicion de Windows: Windows 10 Pro

Comportamiento del computador con respecto a la variacion del numero de particulas que se simulan:
Para obtener el tiempo (en segundos) que se demora el computador en ejecutar el codigo y entregar el grafico, se corrio el codigo para 2, 5, 10 y 20 particulas.

Tiempo por cada numero de particulas:

- Para dos particulas --> tiempo = 2,671

![graf_2p](https://user-images.githubusercontent.com/53713496/66691879-f5bf7100-ec6f-11e9-84a1-bc7a3cb8cf8f.png)

- Para cinco particulas --> tiempo = 29,564

![graf_5p](https://user-images.githubusercontent.com/53713496/66691874-e809eb80-ec6f-11e9-9988-d880bf3288bf.png)

- Para diez particulas --> tiempo = 15,52

![graf_10p](https://user-images.githubusercontent.com/53713496/66691850-aed17b80-ec6f-11e9-91ec-de087c9c75fc.png)

- Para veinte particulas --> tiempo = sin registros.

Para el caso de 20 particula, el computador no fue capaz de arrogar resultado alguno. 

Los graficos anteriores representan el movimiento bidimencional durante 0,5 segundos de particulas ubicadas en el fondo de un rio. El eje "X" de los graficos corresponde al movimiento horizontal de las particulas, y el eje "Y" corresponde al movimiento vertical de ellas, las cuales son desplazadas por accion del agua que va fluyendo por dicho rio. Algunas veces, se puede observar que las particulas cambian so trayectoria drasticamente, lo cual se debe a que en ese punto ocurrio un choque entre particulas. A nivel de codigo, esto se representa con una fuerza k_penal, la cual vendria siendo una constante de penalizacion que se comporta como la fuerza de un rezorte que actua sobre cada particula.

# Analisis de resultados:

Los resultados que nos entrega el codigo no son del todo correctos, ya que en este no se consideran todas las fuerzas que se aplican en la realidad a este tipo de casos ( movimiento de particulas del fondo de un rio).
* fuerzas que se aplican en el codigo:
   * fuerza de gravedad
   * fuerza de arrastre (drag)
   * fuerza de sustentacion (lift)
   * fuerza boyante
* fuerzas que se aplican en la realidad:
   * fuerza de magnus
   * fuerza de basset

# Mejoras en el rendimiento:

Para el caso de las mejoras del computador con respecto a la velocidad de ejecucion del codigo, podriamos implementar otro tipo de integracion. Para la segunda entrega, el metodo que se utilizo para integrar los parametros de las posiciones y las velocidades fue el metodo de Euler, y para la tercera entrega, el metodo de integracion que se utilizo fue odeint.
para lograr una mejor ejecucion del codigo final, podriamos utilizar una nueva libreria, la cual nos permita integrar mas rapidamente los parametros de velocidad y posicion de cada particula, para que asi el comoputador sea capaz de procesar los datos mas rapidamente.

Los cuellos de botella se producen cuando el computador recorre los ciclos del codigo para ver en que momento ocurren choques entre particulas, y es ahi en donde el computador se demora en porcesar la informacion, lo cual produce que a veces no se pueda obtener resultados. esto lo podemos ver en el caso de 20 particulas, ya que al aumentar el numero de particulas, aumenta la probabilidad de que haya choques entre particulas y es por eso que no es capaz de procesar toda esta informacion en un tiempo prudente.

# Resultados del profesor:
* Para dos particulas:

![graf_2prof](https://user-images.githubusercontent.com/53713496/66692124-c27de180-ec71-11e9-9927-50e9a04d55d9.png)

* Para cinco particulas:

![graf_5prof](https://user-images.githubusercontent.com/53713496/66692129-c9a4ef80-ec71-11e9-876d-f26b245d6a99.png)

* Para diez particulas:

![graf_10prof](https://user-images.githubusercontent.com/53713496/66692131-ce69a380-ec71-11e9-95a8-2f212b1a8dc6.png)

* Para veinte particulas:

![particle_trajectories](https://user-images.githubusercontent.com/53713496/66692219-a464b100-ec72-11e9-93c6-674eb51201a7.png)
