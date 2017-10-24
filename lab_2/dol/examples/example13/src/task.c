#include <stdio.h>

#include "task.h"

void task_init(DOLProcess *p) {
    sprintf(p->local->name, "task_%d", GETINDEX(0));
    p->local->index = 0;
}

int task_fire(DOLProcess *p) {
    if (p->local->index < 10) {
        printf("%s: %d\n", p->local->name, p->local->index++);
    }

    if (p->local->index >= 10) {
        DOL_detach(p);
    }

    return 0;
}

