#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to pointer of the head of the list
 */
void reverse_listint(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to pointer of the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head;
    listint_t *fast_ptr = *head;
    listint_t *second_half = NULL;
    listint_t *prev_of_slow_ptr = *head;
    int is_palindrome = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        while (fast_ptr != NULL && fast_ptr->next != NULL)
        {
            fast_ptr = fast_ptr->next->next;
            prev_of_slow_ptr = slow_ptr;
            slow_ptr = slow_ptr->next;
        }

        if (fast_ptr != NULL)
        {
            slow_ptr = slow_ptr->next;
        }

        second_half = slow_ptr;
        reverse_listint(&second_half);
        while (second_half != NULL)
        {
            if ((*head)->n != second_half->n)
            {
                is_palindrome = 0;
                break;
            }
            *head = (*head)->next;
            second_half = second_half->next;
        }

        reverse_listint(&slow_ptr);
        prev_of_slow_ptr->next = slow_ptr;
    }

    return (is_palindrome);
}
