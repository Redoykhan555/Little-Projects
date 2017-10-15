#include <iostream>
#include <string>
#include <vector>
using namespace std;

void print(vector <double> array){
	for(int i=0;i<array.size();i++){
		cout<<array[i]<<endl;
	}
}

int random_partition(vector <double> &A,int p, int r){
	int temp,i;
	double x=A[r];
	i=p-1;
	for(int j=p;j<r;j++){
		if (A[j]<=x){
			i++;
			temp=A[j];
			A[j]=A[i];
			A[i]=temp;
		}
	}
	temp=A[i+1];
	A[i+1]=A[r];
	A[r]=temp;

	return i+1;
}


double RandomSelect(vector <double> A,int p,int r,int i){
	int q,k;
	if (p==r){
		return A[p];
	}
	q=random_partition(A,p,r);
	//print(A);
	k=q-p+1;
	if (i==k-1){
		return A[q];
	}
	else if (i<k-1){
		return RandomSelect(A,p,q-1,i);
	}
	else {
		return RandomSelect(A,q+1,r,i-k);
	}
}

int main(){
	vector <double> list,bucket;
	int i,t;
	double num;

	list.push_back(8);
	list.push_back(2);
	list.push_back(9);
	list.push_back(1);
	list.push_back(10);
	list.push_back(18);
	list.push_back(4);
	list.push_back(9);
	list.push_back(3);
	list.push_back(12);
	list.push_back(5);

	i=6;
	//num=RandomSelect(list,0,list.size()-1,i);
	num=RandomSelect(list,0,10,5);
	cout<<num<<endl;
	return 0;
}