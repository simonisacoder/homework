#ifndef TASK_H
#define TASK_H

#include <dol.h>

typedef struct _local_states {
    char name[10];
    int index;
    int len;
} Task_State;

void task_init(DOLProcess *);
int task_fire(DOLProcess *);

#endif
