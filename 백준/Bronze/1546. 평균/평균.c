
#include <stdio.h>

int main() {
    int n;
    double m = 0.0;
    scanf("%d", &n);
    int an[n];
    double arr[n];
    double cnt = 0.0;
    for(int i = 0;i<n;i++){
        scanf("%d", &an[i]);
        m = (m < an[i] ? an[i] : m);
    }
    for(int i = 0;i<n;i++){
        cnt += (an[i] / m) * 100;
    }
    printf("%lf", cnt / n);
    return 0;
}