#include <stdio.h>

#include "square.h"

void square_init(DOLProcess *p) {
    p->local->index = 0;
    p->local->len = LENGTH;
}

int square_fire(DOLProcess *p) {
    float *i, *j;

    if (p->local->index < p->local->len) {
        DOL_capture((void*)PORT_IN, &i, sizeof(float), p);
        DOL_reserve((void*)PORT_OUT, &j, sizeof(float), p);
        *j = *i * *i;
        DOL_consume((void*)PORT_IN, p);
        DOL_release((void*)PORT_OUT, p);
        p->local->index++;
    }

    if (p->local->index >= p->local->len) {
        DOL_detach(p);
        return -1;
    }

    return 0;
}

