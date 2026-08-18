/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: joserome <joserome@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/01 22:07:22 by joserome          #+#    #+#             */
/*   Updated: 2026/07/24 13:05:44 by joserome         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

static char	*ft_read_and_store(int fd, char *stash)
{
	char	*buffer;
	char	*tmp;
	int		bytes_read;

	if (!stash)
		stash = ft_strdup("");
	if (!stash)
		return (NULL);
	buffer = malloc(BUFFER_SIZE + 1);
	if (!buffer)
		return (free(stash), NULL);
	bytes_read = 1;
	while (!ft_strchr(stash, '\n') && bytes_read > 0)
	{
		bytes_read = read(fd, buffer, BUFFER_SIZE);
		if (bytes_read == -1)
			return (free(stash), free(buffer), NULL);
		buffer[bytes_read] = '\0';
		tmp = stash;
		stash = ft_strjoin(tmp, buffer);
		free(tmp);
		if (!stash)
			return (free(buffer), NULL);
	}
	return (free(buffer), stash);
}

static char	*ft_extract_line(char *stash)
{
	char	*nl;
	int		len;

	nl = ft_strchr(stash, '\n');
	if (nl)
		len = nl - stash + 1;
	else
		len = ft_strlen(stash);
	return (ft_substr(stash, 0, len));
}

static char	*ft_extract_rest(char *stash)
{
	char	*nl;
	int		start;
	int		end;

	nl = ft_strchr(stash, '\n');
	if (!nl)
		return (ft_strdup(""));
	start = nl - stash + 1;
	end = ft_strlen(stash);
	return (ft_substr(stash, start, end - start));
}

char	*get_next_line(int fd)
{
	static char	*stash[1024];
	char		*str;
	char		*tmp;

	if (fd < 0 || fd >= 1024 || BUFFER_SIZE <= 0)
		return (NULL);
	stash[fd] = ft_read_and_store(fd, stash[fd]);
	if (!stash[fd] || !stash[fd][0])
	{
		free(stash[fd]);
		stash[fd] = NULL;
		return (NULL);
	}
	str = ft_extract_line(stash[fd]);
	if (!str)
	{
		free(stash[fd]);
		stash[fd] = NULL;
		return (NULL);
	}
	tmp = stash[fd];
	stash[fd] = ft_extract_rest(tmp);
	if (!stash[fd])
		return (free(tmp), free(str), NULL);
	return (free(tmp), str);
}
