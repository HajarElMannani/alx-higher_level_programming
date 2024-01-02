#include "lists.h"
/**
 *check_cycle - function that checks if a singly linked list has a cycle.
 *@list: linked list to check for cycle in.
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *ptr;
if (list == NULL)
return (0);
while (list != NULL)
{
ptr = list;
list = list->next;
if (ptr <= list)
{
return (1);
}
}
return (0);
}
