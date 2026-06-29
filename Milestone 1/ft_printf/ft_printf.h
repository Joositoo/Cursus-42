/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/17 15:39:43 by joserome          #+#    #+#             */
/*   Updated: 2026/06/19 00:10:57 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>

int	ft_printf(char const *format, ...);
int	ft_parser(char c, va_list args);
int	ft_print_char(int c);
int	ft_print_str(char *str);
int	ft_print_ptr(void *ptr);
int	ft_print_digit(int nb);
int	ft_print_unsigned(unsigned int nb);
int	ft_print_hex(unsigned int nb);
int	ft_print_hex_upper(unsigned int nb);
#endif