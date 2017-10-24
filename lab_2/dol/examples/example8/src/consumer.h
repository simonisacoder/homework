#ifndef CONSUMER_H
#define CONSUMER_H

#include <dol.h>

#define PORT_INA "A"
#define PORT_INB "B"

typedef struct _local_states {
    char name[10];
} Consumer_State;

void consumer_init(DOLProcess *);
int consumer_fire(DOLProcess *);

#endif
