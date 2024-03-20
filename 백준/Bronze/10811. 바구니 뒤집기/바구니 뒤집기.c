#include <stdio.h>

int main() {
    int n,m,a,b;
    scanf("%d %d", &n, &m);
    int arr[n+1];
    for(int i = 1;i<=n;i++){
        arr[i] = i;
    }
    for(int i = 0;i<m;i++){
        int temp = 0;
        scanf("%d %d", &a, &b);
        int s = b - a;
        for(int j = 0;j<(s + 1) / 2;j++){
            temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
            a += 1;
            b -= 1;
        }
    }
    for(int i = 1;i<=n;i++){
            printf("%d ", arr[i]);
        }
    
    return 0;
}