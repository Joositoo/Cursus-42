/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 13:01:59 by joserome          #+#    #+#             */
/*   Updated: 2026/06/09 13:06:31 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Applies the function 'f' to each character of 's', passing its index
** as the first argument, and creates a new string with the results.
** Returns the new string, or NULL if allocation fails or 's' is NULL.
*/

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	int		len;
	int		i;
	char	*arr;

	if (s == NULL)
		return (NULL);
	len = ft_strlen(s);
	arr = malloc(len +1);
	if (arr == NULL)
		return (NULL);
	i = 0;
	while (s[i])
	{
		arr[i] = f(i, s[i]);
		i++;
	}
	arr[i] = '\0';
	return (arr);
}
