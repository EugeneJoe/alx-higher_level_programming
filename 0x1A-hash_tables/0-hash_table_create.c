#include <stdlib.h>
#include "hash_tables.h"

/**
 * hash_table_create - create a new hash table
 * @size: number of hash_node_t nodes in the table
 *
 * Return: pointer to new table or NULL if unsuccessful
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *new_table = NULL;
	unsigned long int idx = 0, j = 0;

	new_table = malloc(sizeof(hash_table_t));
	if (new_table == NULL)
	{
		free(new_table);
		return (NULL);
	}

	new_table->size = size;
	new_table->array = malloc(sizeof(hash_node_t *) * size);
	if (new_table->array == NULL)
	{
		free(new_table->array);
		free(new_table);
		return (NULL);
	}
	for (idx = 0; idx < size; idx++)
	{
		*(new_table->array + idx) = malloc(sizeof(hash_node_t));
		if (*(new_table->array + idx) == NULL)
		{
			for (j = 0; j < idx; j++)
				free(*(new_table->array + j));
			free(new_table->array);
			free(new_table);
			return (NULL);
		}
		new_table->array[idx]->key = NULL;
		new_table->array[idx]->value = NULL;
		new_table->array[idx]->next = NULL;
	}
	return (new_table);
}
