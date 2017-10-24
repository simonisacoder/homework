#ifndef SQUARE_H
#define SQUARE_H

#include <dol.h>
#include "global.h"

#define PORT_IN  0
#define PORT_OUT 1

void square_init(DOLProcess *);
int square_fire(DOLProcess *);

typedef struct _local_states {
    char name[10];
    int index;
    int len;
    float i;
} Square_State;

#endif
