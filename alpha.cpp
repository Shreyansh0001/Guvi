#include <iostream>
using namespace std;

int main() {
	int num,lim,count=0;
	char a[100],b;
	for(int i=0;(((i>=65)&&(i<=91))||((i>=97)&&(i<=123)));i++)
	{
		a[i]=char(i);
	}
	cin>>b;
	for(int i=0;(((i>=65)&&(i<=91))||((i>=97)&&(i<=123)));i++)
	{
		if(b == a[i])
		{
		cout<<"Alphabet";
		count=1;
		}	
	}
	if(count==0)
	cout<<"No";
	return 0;
}
