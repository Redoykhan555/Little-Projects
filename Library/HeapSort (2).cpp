#include<bits/stdc++.h>
using namespace std;
bool exist(int p,int last)
{
    if(p<=last-1) return true;
    return false;
}

void heapify(int* arr,int i,int last)
{
    int left=i*2+1;
    int right=i*2+2;
    int large=i;
    
    if(exist(left,last) and arr[left]>arr[i]) large=left;
    if(exist(right,last) and arr[right]>arr[large]) large=right;
    if(large!=i) {
        swap(arr[i],arr[large]);
        heapify(arr,large,last);
    }
}

void buildHeap(int* arr,int last)
{
    for(int i=last/2-1;i>=0;i--){
        heapify(arr,i,last);
    }
}
void HeapSort(int* arr,int n)
{
    for(int i=0;i<n;i++){
        buildHeap(arr,n-i);
        swap(arr[0],arr[n-i-1]);
    }
}
int main()
{
    int arr[]={12,6,4,34,90,45,2,78,1121};
    HeapSort(arr,9);
    for(int i=0;i<9;i++) cout<<arr[i]<<endl;
    return 0;
}























