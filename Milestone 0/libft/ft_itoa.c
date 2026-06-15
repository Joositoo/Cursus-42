/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 12:30:44 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:07:09 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Converts the integer 'n' to its string representation.
** Handles negative numbers and INT_MIN (-2147483648).
** Returns the resulting string, or NULL if allocation fails.
*/

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

char	*ft_itoa(int n)
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
