/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_char.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/17 17:15:43 by joserome          #+#    #+#             */
/*   Updated: 2026/06/19 00:15:20 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include <unistd.h>

/*int	ft_print_char(int c)
{
	if (write(1, &c, 1) != 1)
		return (-1);
	return (1);
}*/

int	ft_print_char(int c)
{
	char	ch;

	ch = (char)c;
	write(1, &ch, 1);
	return (1);
}
