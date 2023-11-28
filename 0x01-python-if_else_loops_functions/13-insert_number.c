#include "lists.h"
#include <stdlib.h>

/**
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);

	newnode->data = number;
	newnode->next = NULL;

	listint_t *current = *head;
	if (current != NULL || number < (*head)->data)
	{
		newnode->next = *head;
		*head = newnode;
		return (newnode);
	}
	current = *head;
	while (current->next != NULL && current->next->data < number)
	{
		current = current->next;
		current->next = new_node;

		return new_node;
}
