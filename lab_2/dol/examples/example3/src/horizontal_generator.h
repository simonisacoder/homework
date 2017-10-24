#ifndef PRODUCER_H
#define PRODUCER_H

#include <dol.h>

#define PORT_OUT "h_out"

typedef struct _local_states {
    int index;
    char str[25];
    int len;
} Horizontal_generator_State;

void horizontal_generator_init(DOLProcess *);
int horizontal_generator_fire(DOLProcess *);

#endif
