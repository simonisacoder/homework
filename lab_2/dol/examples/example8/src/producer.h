#ifndef PRODUCER_H
#define PRODUCER_H

#include <dol.h>

#define  PORT_OUTA "A"
#define  PORT_OUTB "B"

typedef struct _local_states {
    int index;
    int len;
    char str[26];
} Producer_State;

void producer_init(DOLProcess *);
int producer_fire(DOLProcess *);

#endif
