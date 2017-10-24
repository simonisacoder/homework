#ifndef CONSUMER_H
#define CONSUMER_H

#include <dol.h>

#define PORT_IN "v_in"

typedef struct _local_states {
    char name[20];
} Vertical_consumer_State;

void vertical_consumer_init(DOLProcess *);
int vertical_consumer_fire(DOLProcess *);

#endif
