#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The value to be inserted into the new node.
 *
 * Return: Pointer to the newly inserted node, or NULL on failure.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *previous, *newNode;

	newNode = malloc(sizeof(listint_t));
	if (newNode == NULL)
		return (NULL);
	current = *head;
	previous = NULL;

	newNode->n = number;
	newNode->next = NULL;

	if (*head == NULL)
	{
		*head = NULL;
		return (*head);
	}

	while (current != NULL && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	if (previous == NULL)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		previous->next = newNode;
		newNode->next = current;
	}

	return (*head);
}
