#include <stdio.h>
#include <math.h>
#include "filter.h"

/**
 * Write zero to feedback output.
 */
void filter_init(DOLProcess *p)
{
  p->local->zero = 0.0;
  p->local->factor = 0.5;
  p->local->firstiteration = 1;
}

/**
 * Filter.
 */
int filter_fire(DOLProcess *p)
{
  if (p->local->firstiteration) {
      DOL_write((void*)PORT_OUTB, &(p->local->zero), sizeof(float), p);
      p->local->firstiteration = 0;
  }

  DOL_read((void*)PORT_INA, &(p->local->inA), sizeof(float), p);
  DOL_read((void*)PORT_INB, &(p->local->inB), sizeof(float), p);
  p->local->out = p->local->inA + p->local->factor * p->local->inB;
  DOL_write((void*)PORT_OUTA, &(p->local->out), sizeof(float), p);
  DOL_write((void*)PORT_OUTB, &(p->local->out), sizeof(float), p);

  return 0;
}
