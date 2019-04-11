#include <iostream>
using namespace std;

int pow(int a,int b)
{
	if (b >= 1)
	{
		return a*pow(a,b-1);
	}else 
	return 1;
}

int main() {
	// your code goes here
	int m,n,c;
	cin>>m>>n;
	c = pow(m,n);
	cout<<c;
	return 0;
}
