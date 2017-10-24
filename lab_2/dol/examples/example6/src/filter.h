#ifndef FILTER_H
#define FILTER_H

#include <dol.h>

#define PORT_INA  "inA"
#define PORT_INB  "inB"
#define PORT_OUTA "outA"
#define PORT_OUTB "outB"

typedef struct _local_states
{
  int firstiteration;
  float inA, inB, out, zero, factor;
} Filter_State;

void filter_init(DOLProcess *);
int filter_fire(DOLProcess *);

#endif
