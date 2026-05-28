/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 13:59:09 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 14:03:08 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_strlen(char	*str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

/*int main(void)
{
    printf("strlen('Hola')       = %d\n", ft_strlen("Hola"));        // 4
    printf("strlen('42 Madrid')  = %d\n", ft_strlen("42 Madrid"));   // 9
    printf("strlen('')           = %d\n", ft_strlen(""));             // 0
    printf("strlen('a')          = %d\n", ft_strlen("a"));            // 1
    printf("strlen('\\n')        = %d\n", ft_strlen("\n"));           // 1
    return (0);
}*/