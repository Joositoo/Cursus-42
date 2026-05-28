/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 15:38:39 by joserome          #+#    #+#             */
/*   Updated: 2026/05/21 15:52:47 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>
#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*arr;
	int	len;
	int	i;

	if (max <= min)
	{
		arr = NULL;
		return (arr);
	}
	len = max - min;
	arr = malloc(len * 4);
	i = 0;
	while (min < max)
	{
		arr[i] = min;
		min++;
		i++;
	}
	return (arr);
}

/*int main(void)
{
    int *range;
    int i;

    // Caso normal
    range = ft_range(1, 5);
    i = 0;
    while (i < 4)
    {
        printf("%d ", range[i]);
        i++;
    }
    printf("\n");
    free(range);

    // Negativos a positivos
    range = ft_range(-3, 3);
    i = 0;
    while (i < 6)
    {
        printf("%d ", range[i]);
        i++;
    }
    printf("\n");
    free(range);

    // min == max → NULL
    range = ft_range(5, 5);
    printf("min==max: %s\n", range == NULL ? "NULL" : "no es NULL");

    // min > max → NULL
    range = ft_range(10, 3);
    printf("min>max:  %s\n", range == NULL ? "NULL" : "no es NULL");

    return (0);
}*/