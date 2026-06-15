/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 12:17:54 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:02:45 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates and returns a copy of 's1' with all leading and trailing
** characters present in 'set' removed.
** Returns NULL if allocation fails or if either parameter is NULL.
*/

char	*ft_strtrim(char const *s1, char const *set)
{
	char	*arr;
	int		len;
	int		start;

	if (s1 == NULL || set == NULL)
		return (NULL);
	if (*s1 == '\0')
		return (ft_strdup(""));
	start = 0;
	while (s1[start] && ft_strchr(set, s1[start]))
		start++;
	len = ft_strlen(s1) - 1;
	while (s1[len] && ft_strchr(set, s1[len]))
		len--;
	arr = ft_substr(s1, start, len - start + 1);
	if (arr == NULL)
		return (NULL);
	return (arr);
}
