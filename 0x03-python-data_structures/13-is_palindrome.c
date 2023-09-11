#include "lists.h"
#include <stddef.h>
#include <stdio.h>
/**
 * is_palindrome - check if the given linked list is a palindrome
 * @head: a pointer to the pointer of the head of the linked list
 * Return: 1 if it is a palindrome, else 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *first;
	int i, index = 0, len;
	char nodes[20];
	char reversed[20];

	first = *head;
	for (i = 0; first != NULL; i++)
	{
		nodes[i] = first->n;
		first = first->next;
	}
	i--;
	len = i;
	while (i >= 0)
	{
		reversed[index] = nodes[i];
		index++;
		i--;
	}

	for (i = 0; i <= len; i++)
	{
		if (nodes[i] != reversed[i])
			return (0);
	}
	return (1);
}
