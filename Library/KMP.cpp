#include <iostream> 
#include <string>

using namespace std;

void failureFunction (string pattern, int *charShift) 
{
	charShift[0] = 0;
	int k = 0;
	for (int i=1; i<pattern.length(); i++) {
		while (k>0 && pattern[k] != pattern[i]) {
			k = charShift[k-1];
		}
		if (pattern[k] == pattern[i]) {
			k++;
		}
		charShift[i] = k;
	}
}

void KMPSearch (string text, string pattern) {
	int patternLen = pattern.length();
	int textLen = text.length();
	int charShift [patternLen];
	failureFunction (pattern, charShift);
	int q=0;
	for(int i=0;i<text.length();i++){
		while (q>0 && pattern[q]!=text[i]){
			q=charShift[q];
		}
		if (text[i]==pattern[q]){
			q++;
		}
		if (q==patternLen){
			cout<<"Match found at : "<<(i-(patternLen-2))<<" Index";
			q=charShift[q-1];
			cout<<endl;
		}
	}

}

int main (void) {
	string text, pattern;
	getline (cin, text);
	getline (cin, pattern);
	KMPSearch (text, pattern);
	return 500;
}