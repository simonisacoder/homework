#ifndef ADDMULT_H
#define ADDMULT_H

#include <dol.h>

#define PORT_FACTOR1 "factor1"
#define PORT_FACTOR2 "factor2"
#define PORT_SUMMAND "summand"
#define PORT_SUM     "sum"

typedef struct _local_states
{
  char id[14];
  float sum;
} Addmult_State;

void addmult_init(DOLProcess *);
int addmult_fire(DOLProcess *);

#endif
