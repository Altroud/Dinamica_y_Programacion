#Ejercicio 1.2 a)
import numpy as np
import matplotlib.pyplot as plt

# Función que verifica si un punto (x, y) cumple la condición x^2 + y^2 >= 1
def cumple_condicion(x, y):
    return x**2 + y**2 >= 1

# Generar una malla de puntos en el rango deseado
x_vals = np.linspace(-2, 2, 400)  # Rango para x
y_vals = np.linspace(-2, 2, 400)  # Rango para y

# Crear una matriz booleana que indica si cada punto cumple la condición
points = np.array([[cumple_condicion(x, y) for y in y_vals] for x in x_vals])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Dibujar el conjunto A en blanco y el complemento en negro
ax.imshow(points, extent=(-2, 2, -2, 2), origin='lower', cmap='binary')
ax.imshow(~points, extent=(-2, 2, -2, 2), origin='lower', cmap='gray', alpha=0.5)

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: x^2 + y^2 ≥ 1}')

# Mostrar el gráfico
plt.show()

#Ejercicio 1.2 b)

# Función que verifica si un punto (x, y) cumple la condición 0 < x^2 + y^2 <= 1
def cumple_condicion(x, y):
    return 0 < x**2 + y**2 <= 1

# Generar una malla de puntos en el rango deseado
x_vals = np.linspace(-1.5, 1.5, 400)  # Rango para x
y_vals = np.linspace(-1.5, 1.5, 400)  # Rango para y

# Crear una matriz booleana que indica si cada punto cumple la condición
points = np.array([[cumple_condicion(x, y) for y in y_vals] for x in x_vals])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Dibujar el conjunto A en blanco
ax.imshow(points, extent=(-1.5, 1.5, -1.5, 1.5), origin='lower', cmap='binary')

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: 0 < x^2 + y^2 ≤ 1}')

# Mostrar el gráfico
plt.show()

#Ejercicio 1.2 c)

# Función que verifica si un punto (x, y) cumple la condición 1 < x^2 + y^2 < 4
def cumple_condicion(x, y):
    return 1 < x**2 + y**2 < 4

# Generar una malla de puntos en el rango deseado
x_vals = np.linspace(-2.5, 2.5, 400)  # Rango para x
y_vals = np.linspace(-2.5, 2.5, 400)  # Rango para y

# Crear una matriz booleana que indica si cada punto cumple la condición
points = np.array([[cumple_condicion(x, y) for y in y_vals] for x in x_vals])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Dibujar el conjunto A en blanco
ax.imshow(points, extent=(-2.5, 2.5, -2.5, 2.5), origin='lower', cmap='binary')

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: 1 < x^2 + y^2 < 4}')

# Mostrar el gráfico
plt.show()

#Ejercicio 1.2 d)

# Función que verifica si un punto (x, y) cumple la condición 1 < x^2 + y^2 < 4
def cumple_condicion(x, y):
    return 1 < x**2 + y**2 < 4

# Generar una malla de puntos en el rango deseado
x_vals = np.linspace(-2.5, 2.5, 400)  # Rango para x
y_vals = np.linspace(-2.5, 2.5, 400)  # Rango para y

# Crear una matriz booleana que indica si cada punto cumple la condición
points = np.array([[cumple_condicion(x, y) for y in y_vals] for x in x_vals])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Dibujar el conjunto A en blanco
ax.imshow(points, extent=(-2.5, 2.5, -2.5, 2.5), origin='lower', cmap='binary')

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: 1 < x^2 + y^2 < 4}')

# Mostrar el gráfico
plt.show()

#Ejercicio 1.2 e)

# Función que verifica si un punto (x, y) cumple las condiciones
def cumple_condicion(x, y):
    return x <= y**2 and x**2 + y**2 <= 1

# Generar una malla de puntos en el rango deseado
x_vals = np.linspace(-1.5, 1.5, 400)  # Rango para x
y_vals = np.linspace(-1.5, 1.5, 400)  # Rango para y

# Crear una matriz booleana que indica si cada punto cumple las condiciones
points = np.array([[cumple_condicion(x, y) for y in y_vals] for x in x_vals])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Dibujar el conjunto A en blanco
ax.imshow(points, extent=(-1.5, 1.5, -1.5, 1.5), origin='lower', cmap='binary')

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: x ≤ y^2, x^2 + y^2 ≤ 1}')

# Mostrar el gráfico
plt.show()

#Ejercicio 1.2 f)

# Función que verifica si un punto (x, y) cumple las condiciones
def cumple_condicion(x, y):
    return y >= x**2 and -1 < x < 1

# Generar una malla de puntos en el rango deseado
x_vals = np.linspace(-1.5, 1.5, 400)  # Rango para x
y_vals = np.linspace(-0.5, 1.5, 400)  # Rango para y

# Crear una matriz booleana que indica si cada punto cumple las condiciones
points = np.array([[cumple_condicion(x, y) for y in y_vals] for x in x_vals])

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Dibujar el conjunto A en blanco
ax.imshow(points, extent=(-1.5, 1.5, -0.5, 1.5), origin='lower', cmap='binary')

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: y ≥ x^2, -1 < x < 1}')

# Mostrar el gráfico
plt.show()

#Ejercicio 1.2 g)

import matplotlib.pyplot as plt

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Configurar etiquetas
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Conjunto A: {(x, y) ∈ R^2: x^2 + y^2 < 0}')

# Mostrar el gráfico
plt.show()
