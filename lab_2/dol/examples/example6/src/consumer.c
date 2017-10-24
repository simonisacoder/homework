#include <stdio.h>

#include "consumer.h"

void consumer_init(DOLProcess *p)
{
  ; //nothing to be done here
}

int consumer_fire(DOLProcess *p)
{
  static int index;
  static float sample;

  for (index = 0; index < 10; index++)
  {
    DOL_read((void*)PORT_IN, &sample, sizeof(float), p);
    printf("%8s:                             Read sample[%02d]: %+6.4f\n",
           "consumer", index, sample);
  }
  return 0;
}

