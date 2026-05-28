/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 12:06:16 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 12:06:16 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}
/*
int main(void) {
    int cociente;
    int resto;

    ft_div_mod(10, 3, &cociente, &resto);
    printf("10 / 3 -> cociente: %d, resto: %d\n", cociente, resto);

    ft_div_mod(20, 4, &cociente, &resto);
    printf("20 / 4 -> cociente: %d, resto: %d\n", cociente, resto);

    ft_div_mod(7, 2, &cociente, &resto);
    printf("7 / 2  -> cociente: %d, resto: %d\n", cociente, resto);
}*/