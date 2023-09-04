#include "lists.h"
/**
 * check_cycle - checks if the given listint_t list is a cycle list
 * @list: a pointer to a given listint_t list
 * Return: 1 if the given listint_t is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{	listint_t *slow = list;
	listint_t *fast = list;

	while (slow != NULL || fast != NULL || fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
