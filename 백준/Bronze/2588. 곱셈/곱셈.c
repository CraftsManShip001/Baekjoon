#include <stdio.h>

int main() {
    int num1,num2,h,t,o;
    scanf("%d", &num1);
    scanf("%d", &num2);
    h = num2/100;
    num2 -= h * 100;
    t = num2/10;
    num2 -= t * 10;
    o = num2;
    printf("%d\n", num1 * o);
    printf("%d\n", num1 * t);
    printf("%d\n", num1 * h);
    num2 = (num1 * o) + (num1 * t * 10) + (num1 * h * 100);
    printf("%d", num2);
    return 0;
}