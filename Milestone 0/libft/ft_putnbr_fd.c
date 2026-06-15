/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/10 12:40:21 by joserome          #+#    #+#             */
/*   Updated: 2026/06/10 13:10:55 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include <unistd.h>

/*
** Writes the integer 'n' to the file descriptor 'fd'.
** Handles negative numbers and INT_MIN (-2147483648).
*/

void	ft_putnbr_fd(int n, int fd)
{
	char	c;

	if (n == -2147483648)
	{
		ft_putstr_fd("-2147483648", fd);
		return ;
	}
	if (n < 0)
	{
		ft_putstr_fd("-", fd);
		n = -n;
	}
	if (n >= 10)
		ft_putnbr_fd((n / 10), fd);
	c = n % 10 + '0';
	write(fd, &c, 1);
}
