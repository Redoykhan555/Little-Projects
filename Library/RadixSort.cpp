#include <vector>
#include <iostream>

using namespace std;

int calc(int x,int d){
    for(int i=0;i<d-1;i++){
        x=x/10;
    }
    x=x%10;
    return x;
}

vector<int> counting(vector<int> arr,int k,int d){
    vector<int> bb,cc;
    int n;
    n=arr.size();
    
    for (int i=0;i<k+1;i++){
        cc.push_back(0);
    }
    for(int i=0;i<n;i++){
        bb.push_back(0);
    }

    for(int i=0;i<n;i++){
        cc[calc(arr[i],d)]=cc[calc(arr[i],d)]+1;
    }

    for(int i=1;i<k+1;i++){
        cc[i]=cc[i]+cc[i-1];
    }

    for(int j=n-1;j>-1;j--){
        bb[cc[calc(arr[j],d)]-1]=arr[j];
        cc[calc(arr[j],d)]--;
    }
    return bb;
}

void RadixSort(vector<int> &array,int d){
    for(int i=0;i<d;i++){
        array=counting(array,9,i+1);
    }
}

int main()
{
    vector<int> arr,ans;
    arr.push_back(2545);
    arr.push_back(54344);
    arr.push_back(3334);
    arr.push_back(2476);
    arr.push_back(23134);
    arr.push_back(35787);
    arr.push_back(453);
    arr.push_back(34345);

    RadixSort(arr,5);
   
    for (int i = 0; i <arr.size(); i++)
        cout << arr[i] << " ";
    return 0;
}