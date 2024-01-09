#include "lists.h"
/**
 *print_dlistint - function that prints all the elements
 *of a dlistint_t list.
 *@h: doubly linked list
 *Return: he number of nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
int n = 0;
while (h != NULL)
{
printf("%d\n", h->n);
n++;
h = h->next;
}
return (n);
}
