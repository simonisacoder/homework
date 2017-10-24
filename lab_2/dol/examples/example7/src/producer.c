#include <stdio.h>
#include <string.h>

#include "producer.h"

/**
 * Returns a random integer in the range between lower_bound and
 * upper_bound, where the bounding values are included in the interval.
 */
int getRandomNumber(int lower_bound, int upper_bound)
{
  return (rand() % (upper_bound - lower_bound + 1)) + lower_bound;
}


void producer_init(DOLProcess *p)
{
  printf("init producer.\n");
}


int producer_fire(DOLProcess *p)
{
  srand(0); //initialize random number generator

  //generate input samples and display them
  printf("producer: samples = { ");

  for (p->local->index = 0; p->local->index < NUMBER_OF_SAMPLES; p->local->index++) {
    p->local->sample[p->local->index] = (float) getRandomNumber(-9, 9);
    if (p->local->index < NUMBER_OF_SAMPLES - 1) {
      printf("%+3.1f, ", p->local->sample[p->local->index]);
    }
    else {
      printf("%+3.1f }\n", p->local->sample[p->local->index]);
    }
  }

  //write samples to output port
  for (p->local->index = 0; p->local->index < NUMBER_OF_SAMPLES; p->local->index++) {
    printf("%8s: Write sample[%02d]: %+6.4f\n",
           "producer", p->local->index, p->local->sample[p->local->index]);
    DOL_write((void*)PORT_OUT, &(p->local->sample[p->local->index]),
            sizeof(float), p);
  }

  DOL_detach(p);
  return -1;
}

