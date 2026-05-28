/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_count_if.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 11:36:29 by joserome          #+#    #+#             */
/*   Updated: 2026/05/26 12:42:06 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_count_if(char **tab, int (*f)(char*))
{
	int	cont;
	int	i;

	cont = 0;
	i = 0;
	while (tab[i])
	{
		if (f(tab[i]) == 1)
			cont++;
		i++;
	}
	return (cont);
}

/*int	empieza_por_a(char *str)
{
	return (str[0] == 'a');
}

// Devuelve 1 si el string tiene más de 3 caracteres
int	mas_de_3(char *str)
{
	int i = 0;
	while (str[i])
		i++;
	return (i > 3);
}

int	main(void)
{
	char *tab[] = {"apple", "banana", "avocado", "kiwi", "apricot", 0};

	printf("Empiezan por 'a': %d\n", ft_count_if(tab, &empieza_por_a));
	// Esperado: 3 (apple, avocado, apricot)

	printf("Más de 3 letras: %d\n", ft_count_if(tab, &mas_de_3));
	// Esperado: 5 (apple, banana, avocado, apricot)

	return (0);
}*/