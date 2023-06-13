/*
 * File: 13-is_palindrome.c
 * Author: Oluwatobiloba Light
 */

#include "lists.h"
#include "stdlib.h"

listint_t *reverse_list(listint_t **head);

/**
 * reverse_list - Reverses a singly linked listint_t
 * @head: A double pointer to the begining of the node
 *        of the list
 *
 * Return: A pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *current = *head, *next, *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A double pointer to a listint_t head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	reverse = reverse_list(&temp);
	middle = reverse;
	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	reverse_list(&middle);
	return (1);
}