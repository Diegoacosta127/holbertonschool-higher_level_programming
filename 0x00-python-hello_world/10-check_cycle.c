#include "lists.h"
/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: list to be checked
  * Return: 0 if there's no cycle, 1 if there is
  */
int check_cycle(listint_t *list)
{
	listint_t *rabbit = list, *turtle = list;

	if (!list)
		return (0);
	while (rabbit->next != NULL && rabbit->next->next != NULL)
	{
		turtle = turtle->next;
		rabbit = rabbit->next->next;
		if (rabbit == turtle)
			return (1);
	}
	return (0);
}
