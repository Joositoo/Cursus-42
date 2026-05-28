/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_foreach.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 11:28:46 by joserome          #+#    #+#             */
/*   Updated: 2026/05/26 12:43:53 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_foreach(int	*tab, int length, void (*f)(int))
{
	int	i;

	i = 0;
	while (i < length)
	{
		f(tab[i]);
		i++;
	}
}

/*#include <stdio.h>

// Imprime el número
void	ft_putnbr(int n)
{
	printf("%d\n", n);
}

int	main(void)
{
	int tab[] = {1, 2, 3, 4, 5};

	printf("--- Números originales ---\n");
	ft_foreach(tab, 5, &ft_putnbr);
	// Esperado: 1 2 3 4 5

	return (0);
}*/