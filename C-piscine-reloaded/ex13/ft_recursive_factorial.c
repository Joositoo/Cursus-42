/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 12:23:49 by joserome          #+#    #+#             */
/*   Updated: 2026/05/26 12:58:27 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	if (nb < 0 || nb > 12)
		return (0);
	if (nb == 0)
		return (1);
	return (nb * ft_recursive_factorial(nb - 1));
}

/*int main(void)
{
    printf("factorial(0)  = %d\n", ft_recursive_factorial(0));   // 1
    printf("factorial(1)  = %d\n", ft_recursive_factorial(1));   // 1
    printf("factorial(5)  = %d\n", ft_recursive_factorial(5));   // 120
    printf("factorial(10) = %d\n", ft_recursive_factorial(10));  // 3628800
    printf("factorial(12) = %d\n", ft_recursive_factorial(12));  // 479001600
    printf("factorial(13) = %d\n", ft_recursive_factorial(13));  // 1932053504
    printf("factorial(-1) = %d\n", ft_recursive_factorial(-1));  // 0 (error)
    return (0);
}*/