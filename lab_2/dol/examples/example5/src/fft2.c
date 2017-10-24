#include <stdio.h>
#include <math.h>
#include "fft2.h"

/**
 * Determines the twiddle factor of this 2-point FFT based on the
 * indices of the process.
 */
void fft2_init(DOLProcess *p)
{
  const float PI = 2.0 * asin(1.0);
  int layer_index = GETINDEX(0);
  int process_index = GETINDEX(1);
  float exponent = 2.0 * PI *
          (float)(process_index % (1 << layer_index)) /
          (float)(1 << (layer_index + 1));

  sprintf(p->local->id, "FFT2_%d_%d",
          GETINDEX(0),
          GETINDEX(1));
  p->local->twiddle_factor.real = cos(exponent);
  p->local->twiddle_factor.imag = -sin(exponent);

  printf("%15s: twiddle_factor %9f + j * %9f\n",
          p->local->id,
          p->local->twiddle_factor.real,
          p->local->twiddle_factor.imag);
}

/**
 * Computes 2-point FFT.
 */
int fft2_fire(DOLProcess *p)
{
  DOL_read((void*)PORT_INA, &(p->local->inA), sizeof(ComplexNumber), p);
  DOL_read((void*)PORT_INB, &(p->local->inB), sizeof(ComplexNumber), p);

  p->local->rotated_inB.real = p->local->inB.real
           * p->local->twiddle_factor.real
           - p->local->inB.imag
           * p->local->twiddle_factor.imag ;
  p->local->rotated_inB.imag = p->local->inB.real
           * p->local->twiddle_factor.imag
           + p->local->inB.imag
           * p->local->twiddle_factor.real;

  p->local->outA.real = p->local->inA.real
           + p->local->rotated_inB.real;
  p->local->outA.imag = p->local->inA.imag
           + p->local->rotated_inB.imag;

  p->local->outB.real = p->local->inA.real
           - p->local->rotated_inB.real;
  p->local->outB.imag = p->local->inA.imag
           - p->local->rotated_inB.imag;

  DOL_write((void*)PORT_OUTA, &(p->local->outA), sizeof(ComplexNumber), p);
  DOL_write((void*)PORT_OUTB, &(p->local->outB), sizeof(ComplexNumber), p);

  /*
  printf("%15s: ", p->local->id);
  printf("%9f + j * %9f, %9f + j * %9f => %9f + j * %9f, %9f + j * %9f\n",
          p->local->inA.real,
          p->local->inA.imag,
          p->local->inB.real,
          p->local->inB.imag,
          p->local->outA.real,
          p->local->outA.imag,
          p->local->outB.real,
          p->local->outB.imag);
  */

  return 0;
}
