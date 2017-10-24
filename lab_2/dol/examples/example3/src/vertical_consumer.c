#include <stdio.h>

#include "vertical_consumer.h"

void vertical_consumer_init(DOLProcess *p) {
    sprintf(p->local->name, "v_consumer");
}

int vertical_consumer_fire(DOLProcess *p) {
    char c;
    DOL_read((void*)PORT_IN, &c, 1, p);
    printf("%s: %c\n", p->local->name, c);

    return 0;
}
