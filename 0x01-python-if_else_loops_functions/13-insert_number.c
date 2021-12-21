#include "lists.h"
/**
  * insert_node - inserts a number into a sorted singly linked list
  * @head: pointer to singly linked list
  * @number: number to be inserted
  * Return: pointer to node inserted, NULL if it fails
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL, *temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;
	if (!*head)
	{
		*head = new_node, (*head)->next = NULL;
		return (new_node);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new_node->n)
			(*head)->next = new_node;
		else
			new_node->next = *head, *head = new_node;
		return (new_node);
	}
	while (temp->next != NULL)
	{
		if (new_node->n < temp->n)
		{
			new_node->next = temp, *head = new_node;
			return (new_node);
		}
		if (((new_node->n > temp->n) &&
					(new_node->n < (temp->next)->n)) ||
				(new_node->n == temp->n))
		{
			new_node->next = temp->next, temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	temp->next = new_node;
	return (new_node);
}
