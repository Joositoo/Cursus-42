/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 12:06:51 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 12:06:51 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_iterative_factorial(int nb)
{
	int	result;

	result = 1;
	if (nb < 0)
		return (0);
	if (nb == 0 || nb == 1)
		return (1);
	while (nb > 1)
	{
		if (result > 2147483647 / nb)
			return (0);
		result *= nb;
		nb--;
	}
	return (result);
}

/*int main(void)
{
    printf("factorial(0)  = %d\n", ft_iterative_factorial(0));   // 1
    printf("factorial(1)  = %d\n", ft_iterative_factorial(1));   // 1
    printf("factorial(5)  = %d\n", ft_iterative_factorial(5));   // 120
    printf("factorial(10) = %d\n", ft_iterative_factorial(10));  // 3628800
    printf("factorial(12) = %d\n", ft_iterative_factorial(12));  // 479001600
    printf("factorial(13) = %d\n", ft_iterative_factorial(13));  // 1932053504
    printf("factorial(-1) = %d\n", ft_iterative_factorial(-1));  // 0 (error)
    return (0);
}*/
