#ifndef GENERATOR_H
#define GENERATOR_H

#include <dol.h>
#include "global.h"

#define  PORT_OUT 1

typedef struct _local_states {
    int index;
    int len;
} Generator_State;

void generator_init(DOLProcess *);
int generator_fire(DOLProcess *);

#endif
