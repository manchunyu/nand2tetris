#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "helper.c"

#define VIRTUAL_MEMORY_SIZE 16
#define SCREEN_ADDRESS 16384
#define KBD_ADDRESS 24576


// typedef struct node {
// 	char* symbol;
// 	int address;
// 	struct node* next;
// } node;


node* load_predefined(void);
void read_label(FILE* file, node* head);


int main(void)
{

	node* table_head = load_predefined();

	//Opening the file
	FILE* file = fopen("./rectangle.txt", "r");
	if (file == NULL)
	{
		return 1;
	}

	read_label(file, table_head);

	// Tesing predefined symbols
	for (node* ptr = table_head; ptr != NULL; ptr = ptr->next)
	{
		printf("%s\n", ptr->symbol);
		printf("%i\n", ptr->address);
	}

	free_table(table_head);
	fclose(file);

	return 0;
}

node* load_predefined(void)
{
	char* PRE_DEFINED_SYMBOLS[] = {"SP", "LCL", "ARG", "THIS", "THAT"};

	node* head = NULL;
	node* prev = NULL;

	int length = sizeof(PRE_DEFINED_SYMBOLS) / sizeof(PRE_DEFINED_SYMBOLS[0]);

	for (int i = 0; i < length; i++)
	{

		node* new_node = malloc(sizeof(node));

		if (new_node == NULL)
		{
			return NULL;
		}

		new_node->address = i;
		new_node->symbol = PRE_DEFINED_SYMBOLS[i];
		new_node->next = NULL;
		
		if (i == 0)
		{
			head = new_node;
		}
		else 
		{
			prev->next = new_node;
		}

		prev = new_node;
	}

	
	for (int i = 0; i < VIRTUAL_MEMORY_SIZE; i++)
	{
		node* new_node = malloc(sizeof(node));	
		if (new_node == NULL)
		{
			return NULL;
		}

		char* buffer = malloc(sizeof(char) * 4);
		if (buffer == NULL)
		{
			return NULL;
		}

		sprintf(buffer, "R%i", i);
		
		new_node->address = i;
		new_node->symbol = buffer;
		
		prev->next = new_node;
		prev = new_node;

	}
	

	node* screen = malloc(sizeof(node));
	screen->address = SCREEN_ADDRESS;
	screen->symbol = "SCREEN";
	screen->next = NULL;
	prev->next = screen;

	node* keyboard = malloc(sizeof(node));
	keyboard->address = KBD_ADDRESS;
	keyboard->symbol = "KBD";
	keyboard->next = NULL;
	screen->next = keyboard;

	return head;
}


void read_label(FILE* file, node* head) 
{
    int char_size = sizeof(char);
    int label_buffer_size = 15;
    char* label_buffer = malloc(char_size * label_buffer_size);

    if (label_buffer == NULL) 
    {
        return;
    }

    char* char_buffer = malloc(char_size);
    if (char_buffer == NULL) 
    {
        free(label_buffer);
        return;
    }

    bool is_label = false;
    int line_counter = 0;
    int label_char_counter = 0;

    while (fgets(char_buffer, char_size + 1, file) != NULL) 
    {
    	printf(char_buffer);
        if (*char_buffer == '(') 
        {
            is_label = true;
            continue;
        } 
        else if (*char_buffer == ')') 
        {

            node* new_node = malloc(sizeof(node));
            if (new_node == NULL) 
            {
                free(char_buffer);
                free(label_buffer);
                return;
            }

            char* label = malloc(char_size * (label_char_counter + 1));
            if (label == NULL) 
            {
                free(new_node);
                free(char_buffer);
                free(label_buffer);
                return;
            }

            label_buffer[label_char_counter] = '\0';
            strcpy(label, label_buffer);

            new_node->symbol = label;
            new_node->address = line_counter + 1;
            new_node->next = NULL;
            append_symbol_table(head, new_node);

            label_char_counter = 0;
            is_label = false;
        } 
        else if (*char_buffer == '\n') 
        {
            line_counter++;
        }

        if (is_label == true && label_char_counter < label_buffer_size - 1) 
        {
            label_buffer[label_char_counter] = *char_buffer;
            label_char_counter++;
        }
    }

    free(char_buffer);
    free(label_buffer);
}


