/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_ptr.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/18 23:17:54 by joserome          #+#    #+#             */
/*   Updated: 2026/06/19 00:22:01 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <stdlib.h>
#include <unistd.h>

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

	write(1, "0x", 2);
	len = ft_strlen(values) - 1;
	while (len >= 0)
	{
		write(1, &values[len], 1);
		len--;
	}
}

static int	ft_fill_values(char *values, unsigned long nbr)
{
	int	count;

	count = 0;
	while (nbr >= 16)
	{
		*values = "0123456789abcdef"[nbr % 16];
		values++;
		count++;
		nbr = nbr / 16;
	}
	*values = "0123456789abcdef"[nbr];
	count++;
	values++;
	*values = '\0';
	return (count);
}

int	ft_print_ptr(void *ptr)
{
	unsigned long	tmp;
	int				count;
	int				digits;
	char			*values;
	char			*start;

	if (!ptr)
	{
		write(1, "(nil)", 5);
		return (5);
	}
	tmp = (unsigned long)ptr;
	digits = ft_count_digits(tmp);
	values = malloc(digits + 1);
	count = 0;
	if (!values)
		return (0);
	start = values;
	count += 2 + ft_fill_values(values, tmp);
	ft_print_values(start);
	free(start);
	return (count);
}
