#include <stdio.h>

#include "generator.h"

/**
 * Returns a random integer in the range between lower_bound and
 * upper_bound, where the bounding values are included in the interval.
 */
int getRandomNumber(int lower_bound, int upper_bound)
{
  return (rand() % (upper_bound - lower_bound + 1)) + lower_bound;
}


void generator_init(DOLProcess *p)
{
  ; //nothing to be done here
}


int generator_fire(DOLProcess *p)
{
  int index;
  CREATEPORTVAR(output_port);

  srand(0); //initialize random number generator

  //generate input coefficients and write them to output ports
  for (index = 0; index < NUMBER_OF_FFT_POINTS; index++)
  {
    p->local->coeffs[index].real = (float)getRandomNumber(-9, 9);
    p->local->coeffs[index].imag = (float)getRandomNumber(-9, 9);

    CREATEPORT(output_port, PORT_INPUT_COEFFICIENTS, 1,
            index, NUMBER_OF_FFT_POINTS);
    printf("%15s: Write to input_coefficients_%d: %9f + j * %9f\n",
           "input_generator", index,
           p->local->coeffs[index].real,
           p->local->coeffs[index].imag);
    DOL_write((void*)output_port, &(p->local->coeffs[index]),
              sizeof(ComplexNumber), p);
  }

  DOL_detach(p);
  return -1;
}

