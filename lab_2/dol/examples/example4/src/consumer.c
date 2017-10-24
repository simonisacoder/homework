#include <stdio.h>

#include "consumer.h"

void output_consumer_init(DOLProcess *p)
{
  ; //nothing to be done here
}

int output_consumer_fire(DOLProcess *p)
{
  CREATEPORTVAR(port);

  for (p->local->row = 0; p->local->row < NUMBER_OF_ROWS_COLS; p->local->row++)
  {
    for (p->local->col = 0; p->local->col < NUMBER_OF_ROWS_COLS; p->local->col++)
    {
      CREATEPORT(port, PORT_MATRIXC, 2,
              p->local->row, NUMBER_OF_ROWS_COLS,
              p->local->col, NUMBER_OF_ROWS_COLS);

      DOL_read((void*)port, &p->local->matrixC_value, sizeof(float), p);
      printf("%15s: matrixC[%d][%d]: %f\n",
             "output_consumer", p->local->row, p->local->col, p->local->matrixC_value);
    }
  }
  return 0;
}

