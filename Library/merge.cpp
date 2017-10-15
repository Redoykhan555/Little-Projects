#include <iostream>
#include <vector>
using namespace std;

void print(vector <int> array){
	for(int i=0;i<array.size();i++){
		cout<<array[i]<<endl;
	}
}

vector <int> merge(vector <int> array){
	vector <int> ans;
	int l,p;
	l=array.size();
	int i=0;
	if (l==1){
		return array;
	}
	else{
		vector <int> ans,left,right;
		p=l/2;
		left.insert(left.end(),array.begin(),array.begin()+p);
		right.insert(right.end(),array.begin()+p,array.end());
		left=merge(left);
		right=merge(right);
		while (ans.size()<l){
			if (left.size()==0 || right.size()==0){
				ans.insert(ans.end(),left.begin(),left.end());
				ans.insert(ans.end(),right.begin(),right.end());
				return ans;
			}
			if (left[0]<right[0]){
				ans.push_back(left[0]);
				left.erase(left.begin(),left.begin()+1);
			}
			else{
				ans.push_back(right[0]);
				right.erase(right.begin(),right.begin()+1);
			}
			i+=1;
		}
		return ans;
	}
}

int main(){
	vector <int> arr;
	arr.push_back(5);
	arr.push_back(2);
	arr.push_back(3);
	arr.push_back(9);
	arr.push_back(0);
	arr.push_back(5);
	arr=merge(arr);
	print(arr);
	return 0;

}
