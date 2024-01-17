#include <stdlib.h>
#include "lists.h"

/**
 *insert_node - function inserts a number into a sorted singly linked list
 *@head: head pointer address
 *@number: inserted num
 *Return: inserted node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = node);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = node;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
