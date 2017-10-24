#include <stdio.h>

#include "square.h"

void square_init(DOLProcess *p) {
    sprintf(p->local->name, "square");
    p->local->index = 0;
    p->local->len = LENGTH;
}

int square_fire(DOLProcess *p) {
    if (p->local->index < p->local->len) {
        DOL_read((void*)PORT_IN, &p->local->i, sizeof(float), p);
        p->local->i = p->local->i + p->local->i;
        DOL_write((void*)PORT_OUT, &p->local->i, sizeof(float), p);
        p->local->index++;
    } else {
        DOL_detach(p);
        return -1;
    }

    return 0;
}

