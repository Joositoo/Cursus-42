/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_params.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 14:30:51 by joserome          #+#    #+#             */
/*   Updated: 2026/05/25 13:12:25 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <unistd.h>

void	ft_putchar(char c);
/*{
	write(1, &c, 1);
}*/

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

void	print_params(int argc, char **argv)
{
	int	i;
	int	j;

	if (argc > 0)
	{
		i = 1;
		while (i < argc)
		{
			j = 0;
			while (argv[i][j])
			{
				ft_putchar(argv[i][j]);
				j++;
			}
			ft_putchar('\n');
			i++;
		}
	}
}

int	main(int argc, char **argv)
{
	int		i;
	int		j;
	char	*aux;

	if (argc > 0)
	{
		i = 1;
		while (i < argc - 1)
		{
			j = 1;
			while (j < argc - i)
			{
				if (ft_strcmp(argv[j], argv[j + 1]) > 0)
				{
					aux = argv[j];
					argv[j] = argv[j + 1];
					argv[j + 1] = aux;
				}
				j++;
			}
			i++;
		}
		print_params(argc, argv);
	}
	return (0);
}
