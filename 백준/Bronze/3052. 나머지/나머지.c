#include <stdio.h>

int main() {
    int arr[10], an[10] = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1}, cnt = 0;
    for(int i = 0;i<10;i++){
        scanf("%d", &arr[i]);
        int flag = 0, num = arr[i] % 42;
        for(int j = 0;j<10;j++){
            if(num == an[j]){
                flag = 1;
                break;
            }
        }
        if(flag == 0){
            an[i] = num;
        }
    }
    for(int i = 0;i<10;i++){
        if(an[i] != -1){
            cnt += 1;
        }
    }
    printf("%d", cnt);
    return 0;
}