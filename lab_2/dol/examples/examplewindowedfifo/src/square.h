#ifndef SQUARE_H
#define SQUARE_H

#include <dol.h>
#include "global.h"

#define PORT_IN  100
#define PORT_OUT 200

typedef struct _local_states {
    int index;
    int len;
} Square_State;

void square_init(DOLProcess *);
int square_fire(DOLProcess *);

#endif
