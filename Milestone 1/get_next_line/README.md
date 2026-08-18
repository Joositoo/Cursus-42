*Este proyecto ha sido creado como parte del currículo de 42 por joserome.*

# get_next_line

## Descripción

`get_next_line` es una función en C que permite leer línea a línea desde un descriptor de archivo (file descriptor). Cada llamada a la función devuelve la siguiente línea del archivo, incluyendo el carácter `\n` si existe, hasta que no haya más contenido que leer, momento en el que devuelve `NULL`.

El proyecto introduce el concepto de **variables estáticas** en C, que permiten que una función recuerde su estado entre llamadas sucesivas, sin necesidad de variables globales.

Prototipo de la función:
```c
char *get_next_line(int fd);
```

## Instrucciones

### Compilación

El proyecto se compila con las flags estándar de 42 y el flag `-D BUFFER_SIZE=n` para definir el tamaño del buffer de lectura:

```bash
cc -Wall -Werror -Wextra -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c -o gnl
```

Si no se especifica `BUFFER_SIZE`, se usará el valor por defecto definido en el header (10).

### Ejecución

La función se puede usar con cualquier descriptor de archivo válido, incluyendo `stdin` (fd = 0):

```c
int     fd;
char    *line;

fd = open("archivo.txt", O_RDONLY);
while ((line = get_next_line(fd)) != NULL)
{
    printf("%s", line);
    free(line);
}
close(fd);
```

### Archivos entregados

| Archivo | Descripción |
|---|---|
| `get_next_line.c` | Función principal y funciones auxiliares de extracción |
| `get_next_line_utils.c` | Funciones de manipulación de strings |
| `get_next_line.h` | Header con prototipos y define de BUFFER_SIZE |

## Algoritmo

La implementación se basa en un **stash estático** (`static char *stash`) que actúa como memoria persistente entre llamadas.

El flujo en cada llamada a `get_next_line` es el siguiente:

1. **Lectura y acumulación** (`ft_read_and_store`): se lee del fd en chunks de `BUFFER_SIZE` bytes, uniendo cada chunk al stash mediante `ft_strjoin`. Se repite hasta encontrar un `\n` en el stash o llegar a EOF.

2. **Extracción de la línea** (`ft_extract_line`): se extrae del stash todo hasta el `\n` inclusive (o hasta el final si no hay `\n`) usando `ft_substr`.

3. **Preservación del resto** (`ft_extract_rest`): lo que queda después del `\n` se guarda de nuevo en el stash, listo para la siguiente llamada.

4. **Retorno**: se devuelve la línea extraída. Si el stash está vacío o es NULL, se devuelve NULL.

Esta arquitectura garantiza que se lee lo mínimo necesario en cada llamada y que el estado de lectura persiste correctamente entre invocaciones.

## Recursos

- [Man page de read()](https://man7.org/linux/man-pages/man2/read.2.html)
- [Variables estáticas en C — GeeksforGeeks](https://www.geeksforgeeks.org/static-variables-in-c/)
- [Gestión de memoria dinámica en C](https://www.learn-c.org/en/Dynamic_allocation)

### Uso de IA

Durante el desarrollo de este proyecto se utilizó IA (Claude de Anthropic) como herramienta de guía en el proceso de aprendizaje. La IA no proporcionó código directamente: en su lugar, ofreció pseudocódigo, explicó conceptos, señaló errores lógicos con preguntas dirigidas y orientó al estudiante para que encontrara las soluciones por sí mismo. El código fue escrito íntegramente por el estudiante, iterando sobre cada función con feedback guiado.

Las partes en las que se utilizó la IA fueron:
- Comprensión del flujo general del algoritmo (pseudocódigo inicial)
- Identificación de errores lógicos (condición del while invertida, orden del `\0` y `strjoin`, memory leaks)
- Revisión de edge cases (NULL en `ft_strchr`, última línea sin `\n`, archivo vacío)