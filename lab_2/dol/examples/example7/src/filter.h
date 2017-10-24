#ifndef FILTER_H
#define FILTER_H

#include <dol.h>
#include "global.h"

#define PORT_INA  "inA"
#define PORT_INB  "inB"
#define PORT_OUTA "outA"
#define PORT_OUTB "outB"

typedef struct _local_states
{
  char id[10]; //will contain "filter_xx"
  int first_invocation;
  int process_index;
  float inA, inB, out, filter_coefficient, zero;
} Filter_State;

void filter_init(DOLProcess *);
int filter_fire(DOLProcess *);

#endif
