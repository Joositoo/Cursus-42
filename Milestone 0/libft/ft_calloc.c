/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 18:39:47 by joserome          #+#    #+#             */
/*   Updated: 2026/06/03 19:15:01 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates memory for 'count' elements of 'size' bytes each
** and initializes all bytes to zero.
** Returns a pointer to the allocated memory, or NULL if allocation fails.
** If 'count' or 'size' is 0, returns a unique pointer passable to free().
*/

void	*ft_calloc(size_t count, size_t size)
{
	void	*arr;

	if (count != 0 && size != 0 && size > (size_t)(-1) / count)
		return (NULL);
	if (count == 0 || size == 0 || (size * count == 0))
		return (malloc(0));
	arr = malloc(count * size);
	if (arr == NULL)
		return (NULL);
	ft_bzero(arr, (count * size));
	return (arr);
}
