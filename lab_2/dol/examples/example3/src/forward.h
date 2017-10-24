#ifndef FORWARD_H
#define FORWARD_H

#include <dol.h>

#define PORT_IN1  "west"
#define PORT_IN2  "north"
#define PORT_OUT1 "east"
#define PORT_OUT2 "south"

typedef struct _local_states {
    char name[20];
} Forward_State;

void forward_init(DOLProcess *);
int forward_fire(DOLProcess *);

#endif
