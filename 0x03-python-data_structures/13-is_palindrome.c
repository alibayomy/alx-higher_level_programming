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
	listint_t *last;
	int len = 0, distance, move;

	last = *head;
	first = *head;
	while (last)
	{
		len++;
		last = last->next;
	}
	distance = len;
	last = *head;
	distance--;
	while (distance > 0)
	{
		move = 0;
		while (move < distance)
		{
			move++;
			last = last->next;
		}
		if (first->n == last->n)
		{
			first = first->next;
			last = first;
			distance = distance - 2;
		}
		else
			return (0);
	}
	return (1);
}
