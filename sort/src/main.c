#include "stdio.h"
#include "qgsort.h"


void print(int *a,int n){
    for(int i=0;i<n;i++){
        printf("%d ",*(a+i));
    }
    printf("\n");
}

int main(){
    int q;
    int a[8]={0,0,2,1,1,2,0,2};
    int b[8]={4,5,6,3,4,5,6,8};
    int c[8]={12,53,2,4,6,123,55,72};
    int n=8;
    int temp[10]={0};
    char s[10]={'\0'};
    printf("1.insertSort 2.MergeSort  3.QuickSort 4.CountSort 5.RadixCountSort 6.ColorSort\n");
    scanf("%d",&q);
    gets(s);
    switch (q) {
        case 1:
            printf("before\n");
            print(c,n);
            insertSort(c,n);
            printf("after\n");
            print(c,n);
            break;
        case 2:
            printf("before\n");
            print(c,n);
            MergeSort(c,0,7,temp);
            printf("after\n");
            print(c,n);
            break;
        case 3:
            printf("before\n");
            print(c,n);
            QuickSort_Recursion(c,0,7);
            printf("after\n");
            print(c,n);
            break;
        case 4:
            printf("before\n");
            print(b,n);
            CountSort(b,n,8);
            printf("after\n");
            print(b,n);
            break;
        case 5:
            printf("before\n");
            print(c,n);
            RadixCountSort(c,n);
            printf("after\n");
            print(c,n);
            break;
        case 6:
            printf("before\n");
            print(a,n);
            ColorSort(a,n);
            printf("after\n");
            print(a,n);
            break;
        default:printf("wrong\n");
    }
    return  0;
}

