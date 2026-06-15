/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/08 11:47:03 by joserome          #+#    #+#             */
/*   Updated: 2026/06/08 12:09:47 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates and returns a new string formed by concatenating 's1' and 's2'.
** Returns NULL if allocation fails or if either string is NULL.
*/

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*arr;
	int		len;
	int		i;

	if (s1 == NULL || s2 == NULL)
		return (NULL);
	len = ft_strlen(s1) + ft_strlen(s2);
	arr = malloc(len + 1);
	if (arr == NULL)
		return (NULL);
	i = 0;
	while (s1[i])
	{
		arr[i] = s1[i];
		i++;
	}
	i = 0;
	while (s2[i])
	{
		arr[ft_strlen(s1) + i] = s2[i];
		i++;
	}
	arr[ft_strlen(s1) + i] = '\0';
	return (arr);
}
