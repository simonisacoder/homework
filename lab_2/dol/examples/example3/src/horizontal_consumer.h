#ifndef CONSUMER_H
#define CONSUMER_H

#include <dol.h>

#define PORT_IN "h_in"

typedef struct _local_states {
    char name[20];
} Horizontal_consumer_State;

void horizontal_consumer_init(DOLProcess *);
int horizontal_consumer_fire(DOLProcess *);

#endif
