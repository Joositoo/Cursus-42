/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 13:13:06 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 13:39:18 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_sqrt(int nb)
{
	int	i;

	if (nb <= 0)
		return (0);
	else if (nb == 1)
		return (1);
	i = 1;
	while (i <= nb / 2)
	{
		if (i * i == nb)
			return (i);
		i++;
	}
	return (0);
}

/*int main(void)
{
    printf("sqrt(0)   = %d\n", ft_sqrt(0));    // 0
    printf("sqrt(1)   = %d\n", ft_sqrt(1));    // 1
    printf("sqrt(4)   = %d\n", ft_sqrt(4));    // 2
    printf("sqrt(9)   = %d\n", ft_sqrt(9));    // 3
    printf("sqrt(16)  = %d\n", ft_sqrt(16));   // 4
    printf("sqrt(25)  = %d\n", ft_sqrt(25));   // 5
    printf("sqrt(2)   = %d\n", ft_sqrt(2));    // 0 (irracional)
    printf("sqrt(3)   = %d\n", ft_sqrt(3));    // 0 (irracional)
    printf("sqrt(8)   = %d\n", ft_sqrt(8));    // 0 (irracional)
    printf("sqrt(-1)  = %d\n", ft_sqrt(-1));   // 0 (error)
    return (0);
}*/