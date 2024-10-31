# CNN

de tensorflow.keras importar modelos, capas

modelo = modelos.Sequential()
modelo.add(capas.Conv2D( 32 , ( 3 , 3 ), activación= 'relu' ,forma_de_entrada=( 256 , 256 , 3 )))
modelo.add(capas.MaxPooling2D(( 2 , 2 )))
modelo.add(capas.Conv2D( 64 , ( 3 , 3 ), activación= 'relu' ))
modelo.add(capas.MaxPooling2D(( 2 , 2 )))
modelo.add(capas.Conv2D( 128 , ( 3 , 3 ), activación= 'relu' ))
modelo.add(capas.MaxPooling2D(( 2 , 2 )))
modelo.add(capas.Conv2D( 128 , ( 3 , 3 ), activación= 'relu' ))
modelo.add(capas.MaxPooling2D(( 2 , 2 )))
modelo.add(capas.Conv2D( 256 , ( 3 , 3 ), activación= 'relu' ))
modelo.add(capas.MaxPooling2D(( 2 , 2 )))
modelo.add(capas.Flatten())
modelo.add(capas.Dense( 256 , activación= 'relu' ))
modelo.add(capas.Dense( 1 , activación= 'sigmoid' ))

En una red neuronal convolucional tenemos múltiples capas, como la capa convolucional, la capa de agrupamiento máximo y la capa densa.

Capa de entrada: esta es la entrada que le damos al modelo, y la cantidad de neuronas en esta capa es igual a la cantidad de características en los datos.
Capa convolucional: esta capa aplica filtros a la imagen de entrada para crear mapas de características, que se utilizan para extraer las características. Cada filtro detecta patrones o características específicos en la imagen.
Capa de agrupación máxima: esta capa se utiliza para reducir el tamaño de la imagen y reducir los cálculos. Conserva las características importantes y, al mismo tiempo, reduce las dimensiones espaciales de los mapas de características.
Capa densa: también conocida como capa completamente conectada, donde cada neurona recibe información de las neuronas de la capa anterior. Se utiliza para cambiar las dimensiones del vector.
Capa de salida: la salida de la capa anterior se introduce en una función softmax o sigmoidea, que la convierte en la puntuación de probabilidad de la clase específica.

En la capa de entrada, se establece la forma de entrada del modelo, luego se agrega una capa convolucional 2D con 32 filtros del tamaño (3*3) y una función de activación ReLU. Los filtros permiten que el modelo aprenda un conjunto diverso de características de la imagen de entrada. El tamaño del filtro captura los patrones y ayuda a aprender características complejas. La función de activación ReLU introduce no linealidad al modelo, lo que le permite aprender las relaciones complejas en los datos y ayuda a aliviar el problema del gradiente de desaparición durante el entrenamiento.

Se agrega una capa de agrupación máxima con el tamaño de agrupación (2*2), lo que reduce las dimensiones espaciales de los mapas de características al tomar el valor máximo dentro de cada ventana en esa escala. Cada capa se repite aproximadamente seis veces en este caso para extraer características cada vez más abstractas de la imagen de entrada.

La capa aplanada se utiliza para convertir la capa en una matriz 1D, que será la entrada de la capa completamente conectada. Luego, se agrega una capa completamente conectada con 64 neuronas y una función de activación ReLU. Finalmente, se utiliza una capa de salida con el número de clases y la función de activación softmax para generar las probabilidades según cada clase.

En general, se utilizan varias capas convolucionales seguidas de capas de agrupamiento máximo para extraer las características, luego se utiliza una capa de aplanamiento para convertir los mapas de características 2D en una matriz 1D y, finalmente, se utilizan dos capas completamente conectadas para la clasificación.
