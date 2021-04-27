#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to head of list
 * @number: number to initialize new node with
 *
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	current = *head;
	temp = current;
	if (current->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current != NULL)
	{
		if (current->n < number)
		{
			temp = current;
			current = current->next;
		}
		else
		{
			temp->next = new;
			new->next = current;
			return (new);
		}
	}
	new->next = NULL;
	temp->next = new;
	return (new);
}
