#ifndef PRODUCER_H
#define PRODUCER_H

#include <dol.h>
#include "stdlib.h"

#define PORT_OUT "out"

typedef struct _local_states
{
  float sample[10];
} Producer_State;

void producer_init(DOLProcess *);
int producer_fire(DOLProcess *);

#endif
