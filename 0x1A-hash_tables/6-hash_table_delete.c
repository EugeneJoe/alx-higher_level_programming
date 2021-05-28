#include <stdlib.h>
#include "hash_tables.h"

/**
 * hash_table_delete - deletes a hash table
 * @ht: pointer to hash_table_t table
 *
 * Return: no return value(void)
 */
void hash_table_delete(hash_table_t *ht)
{
	hash_node_t *curr = NULL, *next = NULL;
	unsigned long int index = 0;

	for (index = 0; index < ht->size; index++)
	{
		curr = ht->array[index];
		while (curr != NULL)
		{
			if (curr->key != NULL)
				free(curr->key);
			if (curr->value != NULL)
				free(curr->value);
			next = curr->next;
			free(curr);
			curr = next;
		}
	}
	free(ht->array);
	free(ht);
}
