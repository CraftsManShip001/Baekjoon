#include <stdio.h>
#include <stdlib.h>
int static compare (const void* first, const void* second)
{
    if (*(int*)first > *(int*)second)
        return 1;
    else if (*(int*)first < *(int*)second)
        return -1;
    else
        return 0;
}

int main() {
    
    int n,m,flag,temp,left,right,middle,num;
    scanf("%d", &n);
    int arr[n];
    for(int i = 0;i<n;i++){
        scanf("%d", &arr[i]);
    }
    scanf("%d",&m);
    int an[m];
    for(int j = 0;j<m;j++){
        scanf("%d", &an[j]);
    }
    qsort(arr,n,sizeof(int),compare);
    for(int j = 0;j<m;j++){
        flag = 0;
        left = 0;
        right = m-1;
        num = an[j];
        while(left <= right){
            middle = (left + right) / 2;
            if(num > arr[middle]){
                left = middle+1;
            }
            else if(num < arr[middle]){
                right = middle-1;
            }
            else{
                flag = 1;
                break;
            }
        }
        printf("%d ", flag);
    }
    
    return 0;
}