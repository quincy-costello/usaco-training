/*
ID: quincy.3
LANG: C
TASK: test
*/
#include <stdio.h>

int main(void)
{
    FILE *fin = fopen("test.in", "r");
    FILE *fout = fopen("test.out", "w");

    int a, b;
    fscanf(fin, "%d %d", &a, &b);
    fprintf(fout, "%d\n", a+b);
    return 0;
}