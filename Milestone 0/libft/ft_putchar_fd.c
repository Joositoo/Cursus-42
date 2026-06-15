/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putchar_fd.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 13:16:40 by joserome          #+#    #+#             */
/*   Updated: 2026/06/09 13:18:46 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"
#include "unistd.h"

/*
** Writes the character 'c' to the file descriptor 'fd'.
*/

void	ft_putchar_fd(char c, int fd)
{
	write(fd, &c, 1);
}
