#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 *
 * @head: The address of head of the sorted singly linked list.
 * @number: Number to be inserted.
 * Return: The address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
	}
	else if (current->n > number)
	{
		new->next = current;
		*head = new;
	}
	else
	{
		while (current->next)
		{
			if (current->next->n > number)
				break;
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}

	return (new);
}
