#include <stdio.h>

#include "horizontal_consumer.h"

void horizontal_consumer_init(DOLProcess *p) {
    sprintf(p->local->name, "h_consumer");
}

int horizontal_consumer_fire(DOLProcess *p) {
    char c;
    DOL_read((void*)PORT_IN, &c, 1, p);
    printf("%s: %c\n", p->local->name, c);

    return 0;
}

