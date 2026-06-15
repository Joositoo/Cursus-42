/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/03 19:16:45 by joserome          #+#    #+#             */
/*   Updated: 2026/06/03 19:28:08 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Duplicates the string 's' by allocating sufficient memory
** and copying its content.
** Returns a pointer to the new string, or NULL if allocation fails.
*/

char	*ft_strdup(const char *s)
{
	int		len;
	char	*arr;
	int		i;

	len = ft_strlen(s);
	arr = malloc(len + 1);
	if (arr == NULL)
		return (NULL);
	i = 0;
	while (s[i])
	{
		arr[i] = s[i];
		i++;
	}
	arr[i] = '\0';
	return (arr);
}
