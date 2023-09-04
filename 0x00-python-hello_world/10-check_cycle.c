#include "lists.h"
/**
 * check_cycle - checks if the given listint_t list is a cycle list
 * @list: a pointer to a given listint_t list
 * Return: 1 if the given listint_t is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{	listint_t *tmp;
	listint_t *head = list;

	while (head)
	{
		head = head->next;
		tmp = list;
		if (head->next == NULL)
			return (0);

		while (tmp != head)
		{
			if (head->next == tmp)
			{
				return (1);
			}
			else
				tmp = tmp->next;
		}
	}
	return (0);
}
