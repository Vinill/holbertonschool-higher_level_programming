#include "lists.h"

/**
 * check_cycle - Verifica si en la lista enlazada que agarro hay un ciclo
 *
 * @list: linked list
 *
 * Return: Si hay ciclo 1, si no hay 0
 */
int check_cycle(listint_t *list)
{
	listint_t *fast_p = list;
	listint_t *slow_p = list;

	if (!list)
		return (0);

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
