#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: the address of the head of the singly linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *p1, *p2, *current, *next;

	if (head == NULL || *head == NULL)
		return (1);

	p2 = NULL;
	current = *head;
	next = NULL;
	while (current)
	{
		next = current->next;
		current->next = p2;
		p2 = current;
		current = next;
	}

	p1 = *head;
	while (p1 && p2)
	{
		if (p1->n != p2->n)
			return (0);
		p1 = p1->next;
		p2 = p2->next;
	}

	return (1);
}
