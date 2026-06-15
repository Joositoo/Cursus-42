/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 16:12:18 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:08:03 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Scans the first 'n' bytes of the memory area 'src' for the first
** occurrence of the byte 'c'.
** Returns a pointer to the matching byte, or NULL if not found.
*/

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	tmp;

	if (n == 0)
		return (NULL);
	i = 0;
	tmp = (unsigned char)c;
	while (i < n)
	{
		if (((unsigned char *)s)[i] == tmp)
			return (&((unsigned char *)s)[i]);
		i++;
	}
	return (NULL);
}
