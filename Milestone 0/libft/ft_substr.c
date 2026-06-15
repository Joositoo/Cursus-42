/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 19:41:26 by joserome          #+#    #+#             */
/*   Updated: 2026/06/08 11:42:05 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates and returns a substring of 's' starting at index 'start'
** with a maximum length of 'len'.
** Returns an empty string if 'start' is beyond the end of 's'.
** Returns NULL if allocation fails or if 's' is NULL.
*/

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*arr;
	size_t	i;
	size_t	s_len;

	if (s == NULL)
		return (NULL);
	s_len = ft_strlen(s);
	if (start >= (unsigned int)s_len)
		len = 0;
	else if (len > s_len - start)
		len = s_len - start;
	arr = malloc(len + 1);
	if (arr == NULL)
		return (NULL);
	i = 0;
	while (i < len && s[start + i])
	{
		arr[i] = s[start + i];
		i++;
	}
	arr[i] = '\0';
	return (arr);
}
