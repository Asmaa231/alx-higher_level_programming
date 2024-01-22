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

/**
 *aux_palind - function checks if palind
 *@head: list head
 *@end: list end
 *Return: no thing  
*/

int aux_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (aux_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->n;
		return (1);
	}
	return (0);
}	
