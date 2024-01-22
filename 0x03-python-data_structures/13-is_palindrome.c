#include "lists.h"
/**
 *is_palindrome - function checks recursive palind or not
 *@head: head list
 *Return: 0 if not palind, 1 if palind
 */

int is_palindrome(listint_t **head);
{
	if (head == NULL || *head == NULL)
		return (1);
	return (aux_palind(head, *head))
}

/****
