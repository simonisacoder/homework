#ifndef PRODUCER_H
#define PRODUCER_H

#include "constants.h"
#include <dol.h>

#define PORT_MATRIXA   "matrixA"
#define PORT_MATRIXB   "matrixB"
#define PORT_ZEROINPUT "zeroinput"

typedef struct _local_states
{
  float matrixA[NUMBER_OF_ROWS_COLS][NUMBER_OF_ROWS_COLS];
  float matrixB[NUMBER_OF_ROWS_COLS][NUMBER_OF_ROWS_COLS];
  int row, col, i;
  float zero;
} Input_generator_State;

void input_generator_init(DOLProcess *);
int input_generator_fire(DOLProcess *);

#endif
