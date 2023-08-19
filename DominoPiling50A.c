#include <stdio.h>
#include <string.h>

int main() {
    char input[1000];
    fgets(input, sizeof(input), stdin);
    // Remove the newline character from the input
    input[strcspn(input, "\n")] = '\0';

    int l[2];
    sscanf(input, "%d %d", &l[0], &l[1]);
    printf("%d\n", (l[0] * l[1]) / 2);
    return 0;
}
