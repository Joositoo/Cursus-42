/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_digit.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/18 20:34:13 by joserome          #+#    #+#             */
/*   Updated: 2026/06/19 00:15:24 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>
#include "ft_printf.h"

static long	ft_count_digits(long n)
{
	int		i;
	long	tmp;

	i = 1;
	if (n < 0)
	{
		n = -n;
		i++;
	}
	tmp = n;
	while (tmp >= 10)
	{
		tmp = tmp / 10;
		i++;
	}
	return (i);
}

static void	ft_fill_arr(char *arr, long n, int digits)
{
	int	neg;

	neg = 0;
	if (n < 0)
	{
		n = -n;
		neg = 1;
	}
	arr[digits] = '\0';
	digits--;
	while (digits >= neg)
	{
		arr[digits] = n % 10 + '0';
		n = n / 10;
		digits--;
	}
	if (neg == 1)
		arr[0] = '-';
}

static char	*ft_itoa(int n)
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

int	ft_print_digit(int nb)
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
