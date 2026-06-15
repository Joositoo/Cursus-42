/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 17:26:50 by joserome          #+#    #+#             */
/*   Updated: 2026/06/03 18:00:16 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Locates the first occurrence of 'needle' in 'haystack',
** searching at most 'len' characters.
** Returns a pointer to the beginning of the match, or NULL if not found.
** Returns 'haystack' if 'needle' is an empty string.
*/

static int	ft_valid(const char *haystack, const char *needle, size_t len)
{
	size_t	j;

	j = 0;
	while (j < len && needle[j])
	{
		if (haystack[j] != needle[j])
			return (0);
		j++;
	}
	if (needle[j] == '\0')
		return (1);
	return (0);
}

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;

	if (*needle == '\0')
		return ((char *)haystack);
	if (len == 0)
		return (0);
	i = 0;
	while (i < len && haystack[i])
	{
		if (haystack[i] == needle[0])
			if (ft_valid(&haystack[i], needle, len - i))
				return ((char *)&haystack[i]);
		i++;
	}
	return (NULL);
}
