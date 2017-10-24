#include <stdio.h>

#include "generator.h"

void generator_init(DOLProcess *p) {
    sprintf(p->local->name, "generator");
    p->local->index = 0;
    p->local->len = LENGTH;
}

int generator_fire(DOLProcess *p) {
    if (p->local->index < p->local->len) {
        p->local->x = (float)p->local->index;
        DOL_write((void*)PORT_OUT, &p->local->x, sizeof(float), p);
        p->local->index++;
    } else {
        DOL_detach(p);
        return -1;
    }

    return 0;
}

