#include <stdio.h>
#include <string.h>

void vuln() {
    char buff[16];
    scanf("%s", buff);
}

void secret() {
    printf("You shouldn't be here ;P\n");
}

int main() {
    vuln();
    return 0;
}