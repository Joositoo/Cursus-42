/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_unsigned.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/18 21:12:22 by joserome          #+#    #+#             */
/*   Updated: 2026/06/19 00:16:34 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdlib.h>
#include <unistd.h>

static long	ft_count_digits(unsigned int n)
{
	int		i;
	long	tmp;

	i = 1;
	tmp = n;
	while (tmp >= 10)
	{
		tmp = tmp / 10;
		i++;
	}
	return (i);
}

static void	ft_fill_arr(char *arr, unsigned int n, int digits)
{
	arr[digits] = '\0';
	digits--;
	while (digits >= 0)
	{
		arr[digits] = n % 10 + '0';
		n = n / 10;
		digits--;
	}
}

static char	*ft_itoa(unsigned int n)
{
	int		digits;
	char	*arr;

	digits = ft_count_digits(n);
	arr = malloc(digits + 1);
	if (arr == NULL)
		return (NULL);
	ft_fill_arr(arr, n, digits);
	return (arr);
}

int	ft_print_unsigned(unsigned int nb)
{
	char	*nb_to_str;
	int		i;

	nb_to_str = ft_itoa(nb);
	if (!nb_to_str)
		return (0);
	i = 0;
	while (nb_to_str[i])
	{
		write(1, &nb_to_str[i], 1);
		i++;
	}
	free(nb_to_str);
	return (i);
}
