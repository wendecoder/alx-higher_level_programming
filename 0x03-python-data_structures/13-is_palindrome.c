#include "lists.h"
#include <stdlib.h>
/**
 *reverse_listint - reverses a linked list
 *@head:pointer to first node
 *Return:address of reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *current_node = *head, *next = NULL, *prev = NULL;

	while (current_node)
	{
		next = current_node->next;
		current_node->next = prev;
		prev = current_node;
		current_node = next;
	}
	*head = prev;
	return (*head);
}
/**
 *is_palindrome - checks whether a linked list is palindrome
 *@head:pointer to first node
 *Return:1 - on success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	size_t size = 0, i;
	listint_t *tmp, *rev, *mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tmp = *head;

	for (size = 0; tmp; size++)
		tmp = tmp->next;
	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;
	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);
	tmp = tmp->next->next;
	rev = reverse_listint(&tmp);
	mid = rev;

	tmp = *head;
	while (rev)
	{
		if (tmp->n != rev->n)
			return (0);
		tmp = tmp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
