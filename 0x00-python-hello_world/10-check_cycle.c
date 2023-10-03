#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle.
 *
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
		return (0);

	slow = list;
	fast = slow->next;

	while (slow != NULL && fast->next != NULL &&
			fast->next->next != NULL)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
