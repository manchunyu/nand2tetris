#include <stdlib.h>

#define VIRTUAL_MEMORY_SIZE 16
#define SCREEN_ADDRESS 16384
#define KBD_ADDRESS 24576

typedef struct node {
	char* symbol;
	int address;
	struct node* next;
} node;

void free_table(node* head);
void append_symbol_table(node* head, node* new_node);


void free_table(node* head)
{
	node* next = NULL;

	for (node* ptr = head; ptr != NULL; ptr = next)
	{
		free(ptr->symbol);
		next = ptr->next;
		free(ptr);
	}
}


void append_symbol_table(node* head, node* new_node)
{
	for (node* ptr = head; ptr != NULL; ptr = ptr->next)
	{
		if (ptr->next == NULL)
		{
			ptr->next = new_node;
			break;
		}	
	}
}
