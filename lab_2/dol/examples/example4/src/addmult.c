#include <stdio.h>
#include "addmult.h"

void addmult_init(DOLProcess *p)
{
  sprintf(p->local->id, "addmult_%d_%d_%d",
          GETINDEX(0),
          GETINDEX(1),
          GETINDEX(2));
}


int addmult_fire(DOLProcess *p)
{
  float factor1, factor2, summand;

  DOL_read((void*)PORT_FACTOR1, &factor1, sizeof(float), p);
  DOL_read((void*)PORT_FACTOR2, &factor2, sizeof(float), p);
  DOL_read((void*)PORT_SUMMAND, &summand, sizeof(float), p);
  p->local->sum = factor1 * factor2 + summand;
  DOL_write((void*)PORT_SUM, &(p->local->sum), sizeof(float), p);

  printf("%15s: %f * %f + %f = %f\n",
         p->local->id, factor1, factor2, summand, p->local->sum);

  return 0;
}

