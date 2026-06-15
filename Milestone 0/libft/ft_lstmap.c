/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/10 19:39:22 by joserome          #+#    #+#             */
/*   Updated: 2026/06/11 12:04:29 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/*
** Iterates through 'lst' and applies 'f' to each node's content,
** building a new list with the results.
** Uses 'del' to free content if a node allocation fails.
** Returns the new list, or NULL if allocation fails.
*/

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*new_lst;
	t_list	*new_node;
	t_list	*last;
	void	*new_content;

	if (!lst || !f || !del)
		return (NULL);
	last = NULL;
	new_lst = NULL;
	new_node = NULL;
	while (lst)
	{
		new_content = f(lst->content);
		new_node = ft_lstnew(new_content);
		if (!new_node)
			return (ft_lstclear(&new_lst, del), NULL);
		if (!new_lst)
			new_lst = new_node;
		else
			last->next = new_node;
		last = new_node;
		lst = lst->next;
	}
	return (new_lst);
}
