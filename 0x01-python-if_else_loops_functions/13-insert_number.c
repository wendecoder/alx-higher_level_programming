#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *insert_node - inserts a node in a sorted linked list
 *@head:pointer to sorted linked list
 *@number:no. to insert
 *Return:address of node created
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	temp = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	else
	{
		/*new value less than existing*/
		if (new_node->n < (*head)->n)
		{
			new_node->next = *head;
			*head = new_node;
			return (new_node);
		}
		else
		{
			temp = temp->next;
			for (; temp->next != NULL; )
			{
				if (number >= temp->n && number <= temp->next->n)
				{
					new_node->next = temp->next;
					temp->next = new_node;
					return (new_node);
				}
				temp = temp->next;
			}
			temp->next = new_node;
			return (new_node);
		}
	}
}
