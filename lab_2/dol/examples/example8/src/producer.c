#include <stdio.h>
#include <string.h>

#include "producer.h"

// initialization function
void producer_init(DOLProcess *p) {
    p->local->index = 0;
    p->local->len = 20;
    sprintf(p->local->str, "abcdefghijklmnopqrstuvwxyz");

}

int producer_fire(DOLProcess *p) {

    if (p->local->index < p->local->len) {
        if (DOL_wtest((void*)PORT_OUTA, 1, p)) {
            DOL_write((void*)PORT_OUTA, &(p->local->str[p->local->index]),
                    1, p);
            printf("p write to port A %c\n",
                    p->local->str[p->local->index]);
        }
        else {
            DOL_write((void*)PORT_OUTB, &(p->local->str[p->local->index]),
                    1, p);
            printf("p write to port B %c\n",
                    p->local->str[p->local->index]);
        }
        p->local->index++;
        return 0;
    }
    else {
        DOL_detach(p);
        return -1;
    }
}

