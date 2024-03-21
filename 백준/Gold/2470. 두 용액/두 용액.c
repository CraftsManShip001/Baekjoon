#include <stdio.h>
#include <stdlib.h>
int compare(const void *a, const void *b) {
    if(*(int*)a > *(int*)b) {
        return 1;
    }
    else if(*(int*)a < *(int*)b) {
        return -1;
    }
    else {
        return 0;
    }
}
int main() {
    int n,l = 0,first = 0,second = 0,num,num_n;
    long int mi = 100000000000;
    scanf("%d", &n);
    int r = n-1;
    int arr[n];
    for(int i = 0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    qsort(arr,n,sizeof(int),compare);
    while(l <r){
        num = arr[l] + arr[r];
        num_n = (num < 0) ? (num * -1) : num;
        if(num_n < mi){
            mi = num_n;
            first = l;
            second = r;
        }
        if(num > 0){
            r -= 1;
        }
        else if(num < 0){
            l += 1;
        }
        else{
            first = l;
            second = r;
            break;
        }
    }
    printf("%d %d", arr[first], arr[second]);
    return 0;
}