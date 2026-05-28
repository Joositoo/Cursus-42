/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 14:06:21 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 15:18:26 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] && s2[i])
	{
		if (s1[i] != s2[i])
			return (s1[i] - s2[i]);
		i++;
	}
	return (s1[i] - s2[i]);
}

/*int main(void)
{
    printf("strcmp('abc', 'abc')  = %d\n", ft_strcmp("abc", "abc"));   //  0
    printf("strcmp('abc', 'abd')  = %d\n", ft_strcmp("abc", "abd"));   // -1
    printf("strcmp('abd', 'abc')  = %d\n", ft_strcmp("abd", "abc"));   //  1
    printf("strcmp('', '')        = %d\n", ft_strcmp("", ""));          //  0
    printf("strcmp('abc', '')     = %d\n", ft_strcmp("abc", ""));       //  1
    printf("strcmp('', 'abc')     = %d\n", ft_strcmp("", "abc"));       // -1
    printf("strcmp('abc', 'abcd') = %d\n", ft_strcmp("abc", "abcd"));   // -1
    printf("strcmp('ABC', 'abc')  = %d\n", ft_strcmp("ABC", "abc"));    // -1
}*/