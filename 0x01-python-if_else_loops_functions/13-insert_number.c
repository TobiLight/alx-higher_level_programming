/*
 * File: 13-insert_number.c
 * Authro: Oluwatobiloba Light
*/

#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A double pointer to a listin_t type
 * @number: Number to be inserted to list
 *
 * Return: address of the new node, or NULL if it failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *curr, *prev;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	curr = *head;
	prev = NULL;

	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		prev->next = new;
		new->next = curr;
	}
	return (new);
}
