# MCOC-Proyecto-2 (individual)
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

# RESULTADOS PARA UNA PARTÍCILA:

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
- Tipo de sistema: SIstema operativo de 64 bits,procesador x64
- Edicion de WIndows: Windows 10 Pro

Comportamiento del computador con respecto a la variacion del numero de particulas que se simulan:
para obtener el tiempo (en segundos) que se demora el computador en ejecutar el codigo y entregar el grafico, se corrio el codigo 3 veces por cada numero de particulas (particula 1 --> 3 resultados de tiempo, particula 2 --> 3 resultados de tiempo, particula 3...)
y se saco un promedio de estos 3 tiempos.

Tiempo por cada numero de particulas:
-para una particula --> tiempo = 0,327
-para dos particula --> tiempo = 1,081
-para tres particula --> tiempo = 2,493
-para cuatro particula --> tiempo = 3,845
-para cinco particula --> tiempo = 6,882
-para seis particula --> tiempo = 12,479
-para siete particula --> tiempo = 18,144
-para ocho particula --> tiempo = 22,926
-para nueve particula --> tiempo = 32,81
-para diez particula --> tiempo = 38,374

los graficos anteriores representan el movimiento bidimencional durante 0,5 segundos de particulas ubicadas en el fondo de un rio, las cuales son desplazadas por accion del agua que va corriendo por dicho rio. Algunas veces, se puede observar que las particulas cmabian so trayectoria drasticamente, lo cual se debe a que en ese punto ocurrio un choque entre particulas. A nivel de codigo, esto se representa con una fuerza k_penal, la cual vendria siendo una constante de penalizacion.......
Para el caso de las mejoras del computador con respecto a la velocidad de ejecucion del codigo, podriamos implementar otro tipo de integracion. Para la segunda entrega, el metodo que se utilizo para integrar los parametros de las posiciones y las velocidades fue el metodo de Euler, y para la tercera entrega, el metodo de integracion que se utilizo fue odeint.
para lograr una mejor ejecucion del codigo final, podriamos utilizar una nueva libreria, la cual nos permita integrar mas rapidamente los parametrod de velocidad y posicion de cada particula, para que asi el comoputador sea capaz de procesar los datos mas rapidamente.
