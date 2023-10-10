#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - Check if a linked list of integers is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *prev, *temp;

	if (head == NULL || *head == NULL)
		return (1);

	fast = *head;
	slow = *head;
	prev = NULL;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast != NULL)
		slow = slow->next;

	while (prev != NULL && slow != NULL)
	{
		if (prev->n != slow->n)
			return (0);
		prev = prev->next;
		slow = slow->next;
	}

	return (1);
}
