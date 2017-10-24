#ifndef PRODUCER_H
#define PRODUCER_H

#include <dol.h>
#include "global.h"
#include "stdlib.h"

#define PORT_OUT "out"

typedef struct _local_states
{
  int index;
  float sample[NUMBER_OF_SAMPLES];
} Producer_State;

void producer_init(DOLProcess *);
int producer_fire(DOLProcess *);

#endif
