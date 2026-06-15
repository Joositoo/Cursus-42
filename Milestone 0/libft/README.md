*Este proyecto ha sido creado como parte del currículo de 42 por \<joserome>\.*

---

# Libft

## Descripción

Libft es una librería en C creada desde cero que reimplementa un conjunto de funciones estándar de la libc, además de añadir funciones adicionales de utilidad general. El objetivo del proyecto es comprender en profundidad cómo funcionan estas funciones implementándolas manualmente, construyendo así una base sólida para los proyectos futuros del cursus de 42.

La librería se divide en tres partes:

- **Parte 1** — Reimplementación de funciones de la libc (manipulación de memoria, cadenas y caracteres).
- **Parte 2** — Funciones adicionales no presentes en la libc o con comportamiento distinto.
- **Parte 3** — Funciones para el manejo de listas enlazadas.

---

## Instrucciones

### Compilación

```bash
make
```

Esto genera el archivo `libft.a` en la raíz del repositorio.

### Reglas del Makefile

| Regla | Descripción |
|-------|-------------|
| `make` / `make all` | Compila la librería |
| `make clean` | Elimina los archivos objeto (.o) |
| `make fclean` | Elimina los archivos objeto y `libft.a` |
| `make re` | Ejecuta fclean y vuelve a compilar |
| `make bonus` | Compila incluyendo las funciones de listas enlazadas |

### Uso en un proyecto

```bash
cc -Wall -Wextra -Werror main.c -L. -lft -o programa
```

---

## Funciones implementadas

### Parte 1 — Funciones de libc

| Función | Descripción |
|---------|-------------|
| `ft_isalpha` | Comprueba si un carácter es una letra |
| `ft_isdigit` | Comprueba si un carácter es un dígito |
| `ft_isalnum` | Comprueba si un carácter es alfanumérico |
| `ft_isascii` | Comprueba si un carácter pertenece al ASCII estándar |
| `ft_isprint` | Comprueba si un carácter es imprimible |
| `ft_strlen` | Devuelve la longitud de una cadena |
| `ft_memset` | Rellena un bloque de memoria con un valor |
| `ft_bzero` | Rellena un bloque de memoria con ceros |
| `ft_memcpy` | Copia un bloque de memoria |
| `ft_memmove` | Copia un bloque de memoria gestionando solapamientos |
| `ft_strlcpy` | Copia una cadena con límite de tamaño |
| `ft_strlcat` | Concatena una cadena con límite de tamaño |
| `ft_toupper` | Convierte un carácter a mayúscula |
| `ft_tolower` | Convierte un carácter a minúscula |
| `ft_strchr` | Busca la primera aparición de un carácter en una cadena |
| `ft_strrchr` | Busca la última aparición de un carácter en una cadena |
| `ft_strncmp` | Compara dos cadenas hasta n caracteres |
| `ft_memchr` | Busca un byte en un bloque de memoria |
| `ft_memcmp` | Compara dos bloques de memoria |
| `ft_strnstr` | Busca una subcadena dentro de otra con límite |
| `ft_atoi` | Convierte una cadena a entero |
| `ft_calloc` | Reserva memoria e inicializa a cero |
| `ft_strdup` | Duplica una cadena |

### Parte 2 — Funciones adicionales

| Función | Descripción |
|---------|-------------|
| `ft_substr` | Extrae una subcadena de una cadena |
| `ft_strjoin` | Concatena dos cadenas en una nueva |
| `ft_strtrim` | Elimina caracteres del inicio y el final de una cadena |
| `ft_split` | Divide una cadena en un array usando un delimitador |
| `ft_itoa` | Convierte un entero a cadena |
| `ft_strmapi` | Aplica una función a cada carácter creando una nueva cadena |
| `ft_striteri` | Aplica una función a cada carácter modificándolo en su lugar |
| `ft_putchar_fd` | Escribe un carácter en un descriptor de archivo |
| `ft_putstr_fd` | Escribe una cadena en un descriptor de archivo |
| `ft_putendl_fd` | Escribe una cadena seguida de salto de línea en un descriptor de archivo |
| `ft_putnbr_fd` | Escribe un entero en un descriptor de archivo |

### Parte 3 — Listas enlazadas (bonus)

| Función | Descripción |
|---------|-------------|
| `ft_lstnew` | Crea un nuevo nodo |
| `ft_lstadd_front` | Añade un nodo al inicio de la lista |
| `ft_lstsize` | Cuenta el número de nodos de la lista |
| `ft_lstlast` | Devuelve el último nodo de la lista |
| `ft_lstadd_back` | Añade un nodo al final de la lista |
| `ft_lstdelone` | Elimina un nodo liberando su contenido |
| `ft_lstclear` | Elimina y libera todos los nodos de la lista |
| `ft_lstiter` | Aplica una función al contenido de cada nodo |
| `ft_lstmap` | Crea una nueva lista aplicando una función a cada nodo |

---

## Recursos

### Documentación y referencias

- [Manual de funciones de C (man pages)](https://www.man7.org/linux/man-pages/)
- [cppreference — C standard library](https://en.cppreference.com/w/c)
- [42 Norminette](https://github.com/42School/norminette)

### Uso de IA

Durante el desarrollo de este proyecto se utilizó IA (Claude de Anthropic) como herramienta de apoyo al aprendizaje. Su uso se limitó a:

- Explicar el comportamiento esperado de cada función antes de implementarla.
- Identificar errores en el código ya escrito por el estudiante, sin proporcionar soluciones directas.
- Resolver dudas conceptuales sobre gestión de memoria, punteros y tipos de datos en C.

En ningún caso se utilizó la IA para generar código directamente. Toda la implementación fue desarrollada de forma independiente.