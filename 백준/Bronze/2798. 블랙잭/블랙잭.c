// Online C compiler to run C program online
#include <stdio.h>

int main() {
    int n, m, sum=0;
    int arr[100];
    scanf("%d%d", &n,&m);
    for(int i = 0; i < n; i++) {
        scanf("%d", arr + i);
    }
    for(int i = 0; i < n ; i++) {
        for(int j = 0; j < n; j++) {
            if(j!=i) {
                for(int k = 0; k < n; k++) {
                    if(k!=j && k!=i) {
                        if(sum < (arr[i]+arr[j]+arr[k]) && (arr[i]+arr[j]+arr[k]) <= m) {
                            sum=arr[i]+arr[j]+arr[k];
                        }
                    }
                }
            }
        }
    }
    printf("%d",sum);
    return 0;
}