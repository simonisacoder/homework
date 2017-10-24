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
  ; //nothing to be done here
}


int producer_fire(DOLProcess *p)
{
  static int index;

  srand(0); //initialize random number generator

  //generate input samples and display them
  printf("producer: samples = { ");

  for (index = 0; index < 10; index++) {
    p->local->sample[index] = (float) getRandomNumber(-9, 9);
    if (index < 9) {
      printf("%+3.1f, ", p->local->sample[index]);
    }
    else {
      printf("%+3.1f }\n", p->local->sample[index]);
    }
  }

  //write samples to output port
  for (index = 0; index < 10; index++) {
    printf("%8s: Write sample[%02d]: %+6.4f\n",
           "producer", index, p->local->sample[index]);
    DOL_write((void*)PORT_OUT, &(p->local->sample[index]),
            sizeof(float), p);
  }

  DOL_detach(p);
  return -1;
}

