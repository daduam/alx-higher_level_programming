#include "lists.h"

/**
 * palindrome_util - checks if a sublist is a palindrome.
 *
 * @head: the address of the head current sublist.
 * @p: the address of the current element to compare.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int palindrome_util(listint_t **head, listint_t *p)
{
	if (p == NULL)
		return (1);
	if (palindrome_util(head, p->next) && (*head)->n == p->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 *
 * @head: the address of the head of the singly linked list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palindrome_util(head, *head));
}
