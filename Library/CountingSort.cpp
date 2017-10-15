#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> counting(vector<int> arr,int k){
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
		cc[arr[i]]=cc[arr[i]]+1;
	}

	for(int i=1;i<k+1;i++){
		cc[i]=cc[i]+cc[i-1];
	}

	for(int j=n-1;j>-1;j--){
		bb[cc[arr[j]]-1]=arr[j];
		cc[arr[j]]--;
	}
	return bb;
}

int main(){
	vector<int> arr;
	arr.push_back(2);
	arr.push_back(5);
	arr.push_back(3);
	arr.push_back(0);
	arr.push_back(2);
	arr.push_back(3);
	arr.push_back(0);
	arr.push_back(3);
	vector<int> array;
	int t;
	array=counting(arr,5);
	for(int i=0;i<array.size();i++){
		cout<<array[i]<<' ';
	}
	cin>>t;
	return 0;
}
