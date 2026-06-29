/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_hex_upper.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/18 23:02:44 by joserome          #+#    #+#             */
/*   Updated: 2026/06/19 00:21:44 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>
#include <stdlib.h>

static size_t	ft_strlen(const char *str)
{
	size_t	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

static long	ft_count_digits(long n)
{
	int		i;

	i = 1;
	while (n >= 16)
	{
		n = n / 16;
		i++;
	}
	return (i);
}

static void	ft_print_values(char *values)
{
	int		len;

	len = ft_strlen(values) - 1;
	while (len >= 0)
	{
		write(1, &values[len], 1);
		len--;
	}
}

int	ft_print_hex_upper(unsigned int nb)
{
	int		count;
	int		digits;
	int		i;
	char	*values;

	count = 0;
	digits = ft_count_digits(nb);
	values = malloc(digits + 1);
	if (!values)
		return (0);
	i = 0;
	while (nb >= 16)
	{
		values[i] = "0123456789ABCDEF"[nb % 16];
		i++;
		count++;
		nb = nb / 16;
	}
	values[i] = "0123456789ABCDEF"[nb];
	i++;
	values[i] = '\0';
	count++;
	ft_print_values(values);
	free(values);
	return (count);
}
