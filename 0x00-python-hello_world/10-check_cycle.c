#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 *check_cycle - function checks if cycl happens
 *@list: list pointer to check
 *Return: 1 if cycl happens or 0 if not
*/

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
