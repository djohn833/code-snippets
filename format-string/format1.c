#include <stdio.h>

int target;

void vuln(char *string)
{
    printf(string);

    if (target) {
        printf("you have modified the target :)\n");
    }
}

int main(int argc, char **argv)
{
    vuln(argv[1]);
    return 0;
}
