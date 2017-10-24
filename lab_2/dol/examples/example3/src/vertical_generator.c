#include <stdio.h>
#include <string.h>

#include "vertical_generator.h"

// initialization function
void vertical_generator_init(DOLProcess *p) {
    sprintf(p->local->str,"abcdefghijklm");
    p->local->index = 0;
    p->local->len = strlen(p->local->str);
}

int vertical_generator_fire(DOLProcess *p) {

    if (p->local->index < p->local->len) {
        DOL_write((void*)PORT_OUT, (p->local->str + p->local->index), 1, p);
        p->local->index++;
    } else {
        DOL_detach(p);
    }

    return 0;
}
