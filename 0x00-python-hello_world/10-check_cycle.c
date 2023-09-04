#include "lists.h"
/**
 * check_cycle - checks if the given listint_t list is a cycle list
 * @list: a pointer to a given listint_t list
 * Return: 1 if the given listint_t is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp;
	listint_t *head = list;

	while (head)
	{
		tmp = list;
		head = head->next;
		if (head  == tmp)
		{
			return (1);
		}
		else
		{
			while (tmp != head)
			{
				tmp = tmp->next;
				if (head == tmp)
					return (1);
			}
		}
	}
	return (0);
}
