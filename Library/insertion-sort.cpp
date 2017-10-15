#include <iostream>
#include <string>
#include <vector>
using namespace std;

void insert(vector <int> &arr){
	for (int i=0;i<arr.size();i++){
		int current=arr[i];
		int k=i;
		while (k>0 and current<arr[k-1]){
			arr[k]=arr[k-1];
			k=k-1;
		}
		arr[k]=current;
	}

}