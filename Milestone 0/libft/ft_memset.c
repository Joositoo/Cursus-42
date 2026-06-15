/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 16:03:32 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:07:47 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Fills the first 'n' bytes of the memory area pointed to by 'ptr'
** with the constant byte 'c'.
** Returns a pointer to the memory area 'ptr'.
*/

void	*ft_memset(void *ptr, int c, size_t n)
{
	size_t			i;
	unsigned char	*tmp;

	tmp = ptr;
	i = 0;
	while (i < n)
	{
		tmp[i] = (unsigned char)c;
		i++;
	}
	return (ptr);
}
