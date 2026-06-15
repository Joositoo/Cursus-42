/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/09 11:29:44 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:06:07 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Allocates and returns an array of strings obtained by splitting 's'
** using the character 'c' as a delimiter.
** The array is terminated by a NULL pointer.
** Returns NULL if 's' is NULL or if allocation fails.
*/

static int	ft_count_words(char const *s, char c)
{
	int	i;
	int	count;

	i = 0;
	count = 0;
	while (s[i])
	{
		if (s[i] != c)
		{
			count++;
			while (s[i] && s[i] != c)
				i++;
		}
		else
			i++;
	}
	return (count);
}

static int	ft_fill_arr(char const *s, char c, char **arr)
{
	int	i;
	int	j;
	int	start;

	i = 0;
	j = 0;
	while (s[i])
	{
		if (s[i] != c)
		{
			start = i;
			while (s[i] && s[i] != c)
				i++;
			arr[j] = ft_substr(s, start, i - start);
			if (arr[j] == NULL)
				return (0);
			j++;
		}
		else
			i++;
	}
	arr[j] = NULL;
	return (1);
}

static void	ft_free_arr(char **arr)
{
	int	i;

	i = 0;
	while (arr[i])
	{
		free(arr[i]);
		i++;
	}
	free(arr);
}

char	**ft_split(char const *s, char c)
{
	int		count;
	char	**arr;

	if (s == NULL)
		return (NULL);
	count = ft_count_words(s, c);
	arr = malloc((count + 1) * sizeof(char *));
	if (arr == NULL)
		return (NULL);
	if (ft_fill_arr(s, c, arr) == 0)
	{
		ft_free_arr(arr);
		return (NULL);
	}
	return (arr);
}
