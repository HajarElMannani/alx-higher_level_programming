#include "lists.h"
/**
 *is_palindrome - function in C that checks if a
 * singly linked list is a palindrome
 *@head: first node of the linked list
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
listint_t *ptr;
listint_t *ptr1;
int length, i, j;
i = j = 0;
int a[1024];
if (head == NULL)
return (0);
if (*head == NULL || (*head)->next == NULL)
return (1);
length = 0;
*ptr1 = *head;
while (ptr1->next != NULL)
{
ptr1 = ptr1->next;
length++;
}
while (i <= length)
{
a[i] = ptr->n;
ptr = ptr->next;
i++;
}
while (j < len)
{
if (a[length] != a[j])
{
return (0);
}
j++;
length--;
}
return (1);
}
