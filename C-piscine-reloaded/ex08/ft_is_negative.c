/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 12:02:45 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 12:02:45 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <unistd.h>

void	ft_putchar(char c);
/*{
    write(1, &c, 1);
}*/

void	ft_is_negative(int n)
{
	char	c;

	if (n < 0)
		c = 'N';
	else
		c = 'P';
	ft_putchar(c);
}

/*int main(void) {
    ft_is_negative(-5);    // N
    ft_is_negative(5);     // P
    ft_is_negative(0);     // P
    ft_is_negative(-1);    // N
    ft_is_negative(1000);  // P
    ft_is_negative(-1000); // N
}*/