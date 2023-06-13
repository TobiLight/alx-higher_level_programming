/*
 * File: 13-is_palindrome.c
 * Author: Oluwatobiloba Light
 */

#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

int popint(int *arr, int *size);

/**
 * popint - Pops an element from an array
 * @arr: The array the item is to be popped from
 * @size: The size of the array
 *
 * Return: Popped item or 98 if array is empty
 */
int popint(int *arr, int *size)
{
	if (*size > 0)
	{
		(*size)--;
		return (arr[*size]);
	}
	else
	{
		printf("Array is empty!\n");
	}
	return (98);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A double pointer to a listint_t head
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int *new_arr, popped_int, size = 0, i = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	new_arr = malloc(size * sizeof(int));
	if (new_arr == NULL)
		return (0);
	while (temp)
	{
		new_arr[i] = temp->n;
		temp = temp->next;
		i++;
	}
	temp = *head;
	while (temp)
	{
		popped_int = popint(new_arr, &i);
		if (popped_int != temp->n)
			return (0);
		temp = temp->next;
	}
	free(new_arr);
	return (1);
}
