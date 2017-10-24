#include <stdio.h>

#include "consumer.h"

void consumer_init(DOLProcess *p)
{
  ; //nothing to be done here
}

int consumer_fire(DOLProcess *p)
{
  int index;
  ComplexNumber coeffs[NUMBER_OF_FFT_POINTS];
  CREATEPORTVAR(input_port);

  for (index = 0; index < NUMBER_OF_FFT_POINTS; index++)
  {
    CREATEPORT(input_port, PORT_OUTPUT_COEFFICIENTS, 1,
            index, NUMBER_OF_FFT_POINTS);
    DOL_read((void*)input_port, &coeffs[index], sizeof(ComplexNumber), p);
    printf("%15s: coeff[%d]: %9f + j * %9f\n",
           "output_consumer",
           index, coeffs[index].real, coeffs[index].imag);
  }
  return 0;
}

