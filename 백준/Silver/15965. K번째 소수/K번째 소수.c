#include <stdio.h>

int main() {
    int n,cnt = 0;
    int arr[7368788] = {0,};
    arr[1] = 1;
    scanf("%d", &n);
    for(int i = 2;i<7368788;i++){
        if(arr[i] == 0){
            for(int j = i+i;j<7368788;j+=i){
                arr[j] = 1;
            }
        }
    }
    for(int i = 1;i<7368788;i++){
        if(arr[i] == 0){
            cnt += 1;
        }
        if(cnt == n) {
            printf("%d", i);
            break;
        }
    }
    return 0;
}
