#include <stdio.h>

int main() {
    int n,temp;
    scanf("%d", &n);
    int arr[n];
    for(int i = 0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    for(int i = n;i>0;i--){
        for(int j = 1;j<i;j++){
            if(arr[j] < arr[j-1]){
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }
    for(int l = 0;l<n;l++){
        printf("%d\n", arr[l]);
    }
    return 0;
}