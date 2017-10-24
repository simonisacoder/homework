#include <stdio.h>

#include "consumer.h"

void consumer_init(DOLProcess *p) {
    sprintf(p->local->name, "consumer");
}

int consumer_fire(DOLProcess *p) {
    char c;

    if (DOL_rtest((void*)PORT_INB, 1, p)) {
        DOL_read((void*)PORT_INA, &c, sizeof(char), p);
        printf("from port B: %c\n", c);
        DOL_read((void*)PORT_INA, &c, sizeof(char), p);
        printf("from port A: %c\n", c);
    }

    return 0;
}

