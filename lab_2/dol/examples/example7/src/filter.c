#include <stdio.h>
#include <stdlib.h>
#include "filter.h"

/**
 * Init.
 */
void filter_init(DOLProcess *p)
{
  int k;
  p->local->process_index = GETINDEX(0);

  srand(0); //initialize random number generator
  for (k = 0; k < p->local->process_index; k++)
    rand();

  sprintf(p->local->id, "filter_%d",
          GETINDEX(0));
  p->local->first_invocation = 1;
  //generate a random filter coefficient between -1 and 1
  p->local->filter_coefficient = ((float) (rand() % 21) - 10)/10.0;
  p->local->zero = 0.0;
  printf("init %s: filter coefficient = %+2.1f\n",
         p->local->id, p->local->filter_coefficient);
}

/**
 * Filter.
 */
int filter_fire(DOLProcess *p)
{
  //behaviour of the top filter stage
  if (p->local->process_index == 0) {
    if (p->local->first_invocation) {
      DOL_read((void*)PORT_INA, &(p->local->inA), sizeof(float), p);
      p->local->out = p->local->inA;
      p->local->inB = 0.0;
      p->local->first_invocation = 0;
    }
    else {
      DOL_read((void*)PORT_INA, &(p->local->inA), sizeof(float), p);
      DOL_read((void*)PORT_INB, &(p->local->inB), sizeof(float), p);
      p->local->out = p->local->inB + p->local->inA;
    }

    DOL_write((void*)PORT_OUTA, &(p->local->out), sizeof(float), p);
    DOL_write((void*)PORT_OUTB, &(p->local->out), sizeof(float), p);

    printf("%8s: inA: %6.4f, inB: %6.4f, outA = outB: %6.4f\n",
           p->local->id, p->local->inA, p->local->inB, p->local->out);
  }
  //behaviour of the intermediate filter stages
  else {
    if (p->local->first_invocation) {
      DOL_read((void*)PORT_INA, &(p->local->inA), sizeof(float), p);
      p->local->out = p->local->filter_coefficient * p->local->inA;
      p->local->inB = 0.0;
      p->local->first_invocation = 0;
    }
    else {
      DOL_read((void*)PORT_INA, &(p->local->inA), sizeof(float), p);
      DOL_read((void*)PORT_INB, &(p->local->inB), sizeof(float), p);
      p->local->out = p->local->inB + p->local->filter_coefficient
              * p->local->inA;
    }

    if (p->local->process_index < N - 1) {
      DOL_write((void*)PORT_OUTA, &(p->local->inA), sizeof(float), p);
      DOL_write((void*)PORT_OUTB, &(p->local->out), sizeof(float), p);
    }
    //behaviour of the bottom filter stage
    else {
      DOL_write((void*)PORT_OUTA, &(p->local->zero), sizeof(float), p);
      DOL_write((void*)PORT_OUTB, &(p->local->out), sizeof(float), p);
    }

    printf("%8s: inA: %6.4f, inB: %6.4f, outA: %6.4f, outB: %6.4f\n",
           p->local->id, p->local->inA, p->local->inB, p->local->inA,
           p->local->out);
  }

  return 0;
}
