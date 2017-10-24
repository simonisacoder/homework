#ifndef FFT2_H
#define FFT2_H

#include <dol.h>
#include "global.h"

#define PORT_INA  "inA"
#define PORT_INB  "inB"
#define PORT_OUTA "outA"
#define PORT_OUTB "outB"

typedef struct _local_states
{
  char id[14];
  ComplexNumber inA, inB, outA, outB, rotated_inB, twiddle_factor;
} Fft2_State;

void fft2_init(DOLProcess *);
int fft2_fire(DOLProcess *);

#endif
