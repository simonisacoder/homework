#ifndef CONSUMER_H
#define CONSUMER_H

#include "constants.h"
#include <dol.h>

#define PORT_MATRIXC "matrixC"

typedef struct _local_states
{
  unsigned row, col;
  float matrixC_value;
} Output_consumer_State;

void output_consumer_init(DOLProcess *);
int output_consumer_fire(DOLProcess *);

#endif
