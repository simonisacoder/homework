#include <stdio.h>

#include "forward.h"

void forward_init(DOLProcess *p) {
    sprintf(p->local->name,"Forward");
}

int forward_fire(DOLProcess *p) {
    char c;
    char c2;

    DOL_read((void*)PORT_IN1, &c, 1, p);
    DOL_read((void*)PORT_IN2, &c2, 1, p);
    DOL_write((void*)PORT_OUT1, &c, 1, p);
    DOL_write((void*)PORT_OUT2, &c2, 1, p);

    return 0;
}
