#include <stdio.h>
#include <string.h>

#include "generator.h"

// initialization function
void generator_init(DOLProcess *p) {
    p->local->index = 0;
    p->local->len = LENGTH;
}

int generator_fire(DOLProcess *p) {

    if (p->local->index < p->local->len) {
        float *x;
        DOL_reserve((void*)PORT_OUT, &x, sizeof(float), p);
        *x = (float)p->local->index;
        DOL_release((void*)PORT_OUT, p);
        p->local->index++;
    }

    if (p->local->index >= p->local->len) {
        DOL_detach(p);
        return -1;
    }

    return 0;
}

