#include <stdio.h>
#include <string.h>

#include "generator.h"


Input_generator_State input_generator_state =
  { matrixA: MATRIX_A_INITIAL_VALUE, matrixB: MATRIX_B_INITIAL_VALUE };

void input_generator_init(DOLProcess *p)
{
  for (p->local->row = 0; p->local->row < NUMBER_OF_ROWS_COLS; p->local->row++)
  {
    for (p->local->col = 0; p->local->col < NUMBER_OF_ROWS_COLS; p->local->col++)
    {
      p->local->matrixA[p->local->row][p->local->col] = (NUMBER_OF_ROWS_COLS * p->local->row) + p->local->col + 1;
      p->local->matrixB[p->local->row][p->local->col] = -((NUMBER_OF_ROWS_COLS * p->local->row) + p->local->col);
    }
  }
}


int input_generator_fire(DOLProcess *p)
{
  CREATEPORTVAR(port);

  for (p->local->row = 0; p->local->row < NUMBER_OF_ROWS_COLS; p->local->row++)
  {
    for (p->local->col = 0; p->local->col < NUMBER_OF_ROWS_COLS; p->local->col++)
    {
      CREATEPORT(port, PORT_ZEROINPUT, 1,
              p->local->row * NUMBER_OF_ROWS_COLS + p->local->col, NUMBER_OF_ROWS_COLS
              * NUMBER_OF_ROWS_COLS);
      printf("%15s: Write to zeroinput_%d: %f\n", "input_generator",
             p->local->row * NUMBER_OF_ROWS_COLS + p->local->col, 0.0);
      DOL_write((void*)port, &(p->local->zero), sizeof(float), p);

      for (p->local->i = 0; p->local->i < NUMBER_OF_ROWS_COLS; p->local->i++)
      {
        CREATEPORT(port, PORT_MATRIXA, 3,
                p->local->row, NUMBER_OF_ROWS_COLS,
                p->local->col, NUMBER_OF_ROWS_COLS,
                p->local->i, NUMBER_OF_ROWS_COLS);
        printf("%15s: Write to matrixA_%d_%d_%d: %f\n",
               "input_generator", p->local->i, p->local->row, p->local->col,
               p->local->matrixA[p->local->row][p->local->col]);
        DOL_write((void*)port, &(p->local->matrixA[p->local->row][p->local->col]),
                  sizeof(float), p);
        CREATEPORT(port, PORT_MATRIXB, 3,
                p->local->row, NUMBER_OF_ROWS_COLS,
                p->local->col, NUMBER_OF_ROWS_COLS,
                p->local->i, NUMBER_OF_ROWS_COLS);
        printf("%15s: Write to matrixB_%d_%d_%d: %f\n",
               "input_generator", p->local->i, p->local->row, p->local->col,
               p->local->matrixB[p->local->row][p->local->col]);
        DOL_write((void*)port, &(p->local->matrixB[p->local->row][p->local->col]),
                  sizeof(float), p);
      }
    }
  }

  DOL_detach(p);
  return -1;
}

