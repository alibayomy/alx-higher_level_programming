#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - insert a node into a sorted linked list
 * @head: a pointer to the pointer of the head of the list
 * @number: the number of the node that will be inserted 
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *point = *head;
	listint_t *hold;

	tmp = malloc(sizeof(listint_t));
	if (tmp == NULL)
		return (NULL); 
	tmp->n = number;
	tmp->next = NULL;
	if (point == NULL || (point->n > tmp->n))
	{
		hold = point;
		*head = tmp;
		tmp->next = hold;
		return (tmp);
	}
	while (point->next)
	{
	   if (point->next->n > tmp->n)
	   {
			hold = point->next;
			point->next = tmp;
			tmp->next = hold;
			return (tmp);
	   }
		point = point->next;
	}
	point->next = tmp;
	return (tmp);
}
