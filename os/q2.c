#include <stdio.h>

int main() {
    int n, a = 0, b = 1, next;

    printf("Enter the value of n: ");
    scanf("%d", &n);

    printf("Fibonacci Series up to %d:\n", n);

    while (a <= n) {
        if (a >= 1) {   
            printf("%d ", a);
        }
        next = a + b;
        a = b;
        b = next;
    }

    return 0;
}
