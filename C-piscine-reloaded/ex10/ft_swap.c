/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 12:05:26 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 12:05:26 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

void	ft_swap(int *a, int *b)
{
	int	aux;

	aux = *a;
	*a = *b;
	*b = aux;
}
/*
int main(void) {
    int a;
    int b;

    a = 10;
    b = 20;
    printf("Antes:  a = %d, b = %d\n", a, b);
    ft_swap(&a, &b);
    printf("Despues: a = %d, b = %d\n", a, b);
}*/