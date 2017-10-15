#include <iostream>
#include <vector>
using namespace std;

void maxify( vector <int> &array, int i,int heapSize){
	int left=2*i+1;
	int right=2*i+2;
	int largest=i;
	if (left<heapSize and array[left]>array[i]){
		largest=left;
	}
	
	if (right<heapSize and array[right]>array[largest]){
		largest=right;
	}

	if (i!=largest){
		int temp=array[i];
		array[i]=array[largest];
		array[largest]=temp;
		maxify(array,largest,heapSize);
	} 
}
void buildMaxHeap(vector <int> &array){
	for(int i=array.size()/2;i>=0;i--){
		maxify(array,i,array.size());
	}
}

void HeapSort(vector <int> &array){
	buildMaxHeap(array);
	int heapsize=array.size()-1;
	for(int i=array.size()-1;i>=1;i--){
		int temp=array[0];
		array[0]=array[i];
		array[i]=temp;
		heapsize--;
		//cout<<array[i]<<endl;
		maxify(array,0,heapsize);
	}
}

int main(){
	vector<int> array;
	array.push_back(5);
	array.push_back(3);
	array.push_back(89);
	array.push_back(3543);
	array.push_back(52);
	array.push_back(68);
	array.push_back(234);

	HeapSort(array);
	for (int i=0;i<array.size();i++){
		cout<<array[i]<<endl;
	}
	return 0;
}