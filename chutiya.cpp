#include<iostream>
//#include<algorithm>
using namespace std;
int main()
{
    int n,a,b;
    cin>>n>>a>>b;
    int c = a+b;
    if(n%c ==0)
    cout<<"YES";
    else 
    cout<<"NO";
    return 0;
}
