#ifndef SSUWB_H
#define SSUWB_H
#include "rcmIf.h"
#include "rcm.h"


int* measure();

void ssUWB(char * name, char * port);
void initial();


    int uwb(int destNodeId);




#endif // SSUWB_H
