#include <stdio.h>

int main() {
    int n,cnt = 0;
    for(int i=0;i<5;i++){
        scanf("%d", &n);
        cnt += n*n;
    }
    printf("%d", cnt % 10);
    return 0;
}