/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 16:12:28 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:16:58 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Sets the first 'n' bytes of the memory area pointed to by 'ptr' to zero.
** Returns nothing.
*/

void	ft_bzero(void *ptr, size_t n)
{
	size_t			i;
	unsigned char	*tmp;

	tmp = ptr;
	i = 0;
	while (i < n)
	{
		tmp[i] = 0;
		i++;
	}
}
