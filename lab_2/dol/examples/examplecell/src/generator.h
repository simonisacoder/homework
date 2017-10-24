#ifndef GENERATOR_H
#define GENERATOR_H

#include <dol.h>
#include "global.h"

#define  PORT_OUT 10

void generator_init(DOLProcess *);
int generator_fire(DOLProcess *);

typedef struct _local_states {
    char name[10];
    int index;
    int len;
    float x;
} Generator_State;

#endif
