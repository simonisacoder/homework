#include <stdio.h>
#include <string.h>

#include "horizontal_generator.h"

// initialization function
void horizontal_generator_init(DOLProcess *p) {
    sprintf(p->local->str, "nopqrstuvwxyz");
    p->local->index = 0;
    p->local->len = strlen(p->local->str);
}

int horizontal_generator_fire(DOLProcess *p) {

    if (p->local->index < p->local->len) {
        DOL_write((void*)PORT_OUT, (p->local->str + p->local->index), 1, p);
        p->local->index++;
    }
    else {
        DOL_detach(p);
    }
    return 0;
}

