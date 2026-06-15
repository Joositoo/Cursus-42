/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 18:03:10 by joserome          #+#    #+#             */
/*   Updated: 2026/06/03 19:00:44 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Converts the initial portion of the string 'str' to an integer.
** Skips leading whitespace, handles an optional sign (+ or -),
** and stops at the first non-digit character.
** Returns the converted integer value.
*/

int	ft_atoi(const char *str)
{
	int	number;
	int	sign;

	while (*str == 32 || (9 <= *str && *str <= 13))
		str++;
	sign = 1;
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign = -sign;
		str++;
	}
	number = 0;
	while ('0' <= *str && *str <= '9')
	{
		number = number * 10 + (*str - '0');
		str++;
	}
	return (number * sign);
}
