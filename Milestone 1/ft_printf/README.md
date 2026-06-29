*Este proyecto ha sido creado como parte del currículo de 42 por \<joserome>\.*

# ft_printf

## Descripción

`ft_printf` es una reimplementación de la función `printf()` de la librería estándar de C. El objetivo del proyecto es comprender el funcionamiento interno de las funciones variádicas en C, es decir, funciones que aceptan un número variable de argumentos.

La función está compilada como una librería estática (`libftprintf.a`) que puede integrarse en futuros proyectos en C.

### Conversiones implementadas

| Especificador | Descripción |
|---|---|
| `%c` | Imprime un carácter |
| `%s` | Imprime una cadena de caracteres |
| `%p` | Imprime un puntero en formato hexadecimal |
| `%d` | Imprime un número decimal con signo |
| `%i` | Imprime un entero en base 10 |
| `%u` | Imprime un número decimal sin signo |
| `%x` | Imprime un número hexadecimal en minúsculas |
| `%X` | Imprime un número hexadecimal en mayúsculas |
| `%%` | Imprime el símbolo `%` |

## Instrucciones

### Compilación

```bash
make
```

Esto genera el archivo `libftprintf.a` en la raíz del repositorio.

### Uso en un proyecto

```bash
cc -Wall -Wextra -Werror main.c libftprintf.a -o programa
```

Incluye el header en tu código:

```c
#include "ft_printf.h"

int main(void)
{
    ft_printf("Hola %s, tienes %d años\n", "mundo", 42);
}
```

### Reglas del Makefile

| Regla | Descripción |
|---|---|
| `make` / `make all` | Compila la librería |
| `make clean` | Elimina los archivos objeto |
| `make fclean` | Elimina los archivos objeto y la librería |
| `make re` | Recompila desde cero |

## Algoritmo y estructura de datos

### Estructura general

El proyecto está dividido en ficheros por responsabilidad:

- `ft_printf.c` — función principal, recorre el string de formato carácter a carácter
- `ft_parser.c` — dispatcher que identifica el especificador y llama a la función correspondiente
- `ft_print_*.c` — una función por cada tipo de conversión

### Flujo de ejecución

1. `ft_printf` recorre el string de formato con un índice `i`
2. Si encuentra un `%`, avanza un carácter y llama a `ft_parser` con el especificador y el `va_list`
3. `ft_parser` extrae el argumento con `va_arg` del tipo correcto y llama a la función de impresión
4. Cada función de impresión devuelve el número de caracteres escritos, que se acumula en un contador
5. `ft_printf` devuelve el total de caracteres escritos

### Conversión numérica

Para `%d`/`%i` y `%u` se usa una implementación de `itoa`: se cuenta el número de dígitos, se reserva memoria con `malloc`, se rellena el array de atrás hacia adelante dividiendo entre 10, y se libera con `free` tras escribir.

Para `%x`, `%X` y `%p` el mismo principio pero dividiendo entre 16 y usando la cadena `"0123456789abcdef"` como tabla de lookup para mapear cada resto al carácter hexadecimal correspondiente. Como los dígitos se generan en orden inverso, se almacenan en un array y se imprimen de atrás hacia adelante.

Para `%p` se añade el prefijo `0x` y se trabaja con `unsigned long` para soportar direcciones de 64 bits.

## Recursos

- [man 3 printf](https://man7.org/linux/man-pages/man3/printf.3.html) — documentación oficial de printf
- [man 3 stdarg](https://man7.org/linux/man-pages/man3/stdarg.3.html) — documentación de va_list, va_start, va_arg, va_end
- [printf format string (Wikipedia)](https://en.wikipedia.org/wiki/Printf_format_string) — referencia completa del formato

### Uso de IA

Durante este proyecto se ha utilizado IA (Claude) como herramienta de apoyo al aprendizaje, no para generar código directamente. Su uso se limitó a:
- Explicar conceptos (funciones variádicas, conversión hexadecimal, promoción de tipos en C)
- Identificar bugs en el código propio y orientar hacia la solución
- Resolver dudas sobre comportamiento de `printf` en casos límite (`INT_MIN`, `NULL`, etc.)

Todo el código ha sido escrito e implementado de forma propia.