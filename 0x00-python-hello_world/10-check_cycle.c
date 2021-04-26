#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check if a singly linked list has a cycle in it
 * @list: pointer to list node
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p, *q; /*p - step of 1, q - step of 3*/

	p = list;
	q = list;
	while (p != NULL || q != NULL)
	{
		p = p->next;
		q = q->next->next;
		if (p == NULL || q == NULL)
			return (0);
		if (p == q)
			return (1);
	}
	return (0);
}
