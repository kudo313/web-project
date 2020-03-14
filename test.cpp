#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

struct dllist
{
    int number;
    struct dllist *next;

};

int main()
{
    struct dllist *node, *node1;
    node = (struct dllist *)malloc(sizeof(struct dllist));
    node->number=1;
    node1 = (struct dllist *)malloc(sizeof(struct dllist));
    node->next=node1;
    node1->number=2;
    node1->next=NULL;
    printf("%d",node->number);
    if (node->next->next==NULL){    printf("\n%d",node->next->number);
    }

}