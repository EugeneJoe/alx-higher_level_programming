#include <stdio.h>
#include "hash_tables.h"

/**
 * hash_table_print - prints a hash table
 * @ht: pointer to a hash_table_t table
 *
 * Return: No return value (void)
 */
void hash_table_print(const hash_table_t *ht)
{
	unsigned long int index = 0, size = 0, comma = 0;
	hash_node_t *curr = NULL;

	if (ht == NULL)
		return;

	printf("{");
	size = ht->size;
	for (index = 0; index < size; index++)
	{
		curr = ht->array[index];
		while (curr != NULL)
		{
			if (curr->key == NULL)
				break;
			if (comma == 0)
				comma += 1;
			else
				printf(", ");

			printf("'%s': '%s'", curr->key, curr->value);
			curr = curr->next;
		}
	}
	printf("}\n");
}
