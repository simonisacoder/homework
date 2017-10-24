#ifndef CONSUMER_H
#define CONSUMER_H

#include <dol.h>
#include "global.h"

#define PORT_IN "in"

typedef struct _local_states
{
} Consumer_State;

void consumer_init(DOLProcess *);
int consumer_fire(DOLProcess *);

#endif
