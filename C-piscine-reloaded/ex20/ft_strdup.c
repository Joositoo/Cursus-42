/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 15:01:55 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 15:14:49 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int	ft_strlen(char	*str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	int		i;
	int		len;
	char	*str;

	len = ft_strlen(src);
	str = malloc(len + 1);
	i = 0;
	while (src[i])
	{
		str[i] = src[i];
		i++;
	}
	str[i] = '\0';
	return (str);
}

/*int main(void)
{
    char *original;
    char *copia;

    original = "Hola 42";
    copia = ft_strdup(original);
    printf("original = %s\n", original);
    printf("copia    = %s\n", copia);
    printf("misma direccion? %d\n", original == copia); // 0, son independientes
    free(copia);

    copia = ft_strdup("");
    printf("vacia    = '%s'\n", copia);
    free(copia);

    return (0);
}*/