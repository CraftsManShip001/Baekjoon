#include <stdio.h>

int main() {
    int n = 5,temp,cnt = 0;
    int arr[n];
    for(int i = 0;i<n;i++){
        scanf("%d", &arr[i]);
        cnt += arr[i];
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
    printf("%d\n", cnt / 5);
    printf("%d", arr[2]);
    return 0;
}