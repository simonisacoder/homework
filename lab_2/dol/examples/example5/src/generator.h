#ifndef PRODUCER_H
#define PRODUCER_H

#include <dol.h>
#include "global.h"
#include "stdlib.h"

#define PORT_INPUT_COEFFICIENTS "input_coefficients"

typedef struct _local_states
{
  ComplexNumber coeffs[NUMBER_OF_FFT_POINTS];
} Generator_State;

void generator_init(DOLProcess *);
int generator_fire(DOLProcess *);

#endif
