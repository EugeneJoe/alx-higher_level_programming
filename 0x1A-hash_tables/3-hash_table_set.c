#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "hash_tables.h"

/**
 * add_node_head - adds a new node at the beginning of a list.
 * @head: pointer to head of the linked list hash_node_t
 * @key: key value of hash table entry (string)
 * @value: value associated with key for hash table
 *
 * Return: 1 on success, 0 on failure
 */
int add_node_head(hash_node_t **head, const char *key, const char *value)
{
	hash_node_t *new;

	if (key == NULL)
		return (0);
	new = malloc(sizeof(hash_node_t));
	if (new == NULL)
	{
		free(new);
		return (0);
	}
	new->key = strdup(key);
	new->value = strdup(value);
	new->next = *head;
	*head = new;
	return (1);
}

/**
 * hash_table_set - adds an element to a hash table
 * @ht: pointer to hash table
 * @key: pointer to string that's the key
 * @value: value associated with the key
 *
 * Return: 1 on success, 0 on failure
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int index = 0, res = 0;

	if (key == NULL || ht == NULL || strcmp(key, "") == 0)
		return (0);
	index = key_index((unsigned char *)key, ht->size);

	if (ht->array[index]->key == NULL)
	{
		ht->array[index]->key = strdup(key);
		ht->array[index]->value = strdup(value);
		ht->array[index]->next = NULL;
	}
	else
	{
		res = add_node_head(&(ht->array[index]), key, value);
	}
	if (res == 1)
		return (1);
	else
		return (0);
}
