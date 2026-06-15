/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 18:21:00 by joserome          #+#    #+#             */
/*   Updated: 2026/05/27 18:38:30 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Copies up to 'size' - 1 characters from 'src' to 'dst',
** null-terminating the result.
** Returns the total length of 'src'.
*/

size_t	ft_strlcpy(char *dst, const char *src, size_t n)
{
	size_t	size;
	size_t	i;

	size = 0;
	while (src[size])
		size++;
	if (n == 0)
		return (size);
	i = 0;
	while ((i < n - 1) && src[i])
	{
		dst[i] = src[i];
		i++;
	}
	dst[i] = '\0';
	return (size);
}
