#ifndef PRODUCER_H
#define PRODUCER_H

#include <dol.h>

#define PORT_OUT "v_out"

typedef struct _local_states {
    int index;
    char str[20];
    int len;
} Vertical_generator_State;

void vertical_generator_init(DOLProcess *);
int vertical_generator_fire(DOLProcess *);

#endif
