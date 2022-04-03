#include<iostream>
#include<exception>
///////////////////////  EXCEPTION/CATCH/TRY  ///////////////////////////
using namespace std;

class myexception : public exception{
	public:
		const char * what() const throw()
		//the throw keyword throws an exception when a problem is detected which lets us create a custom error
	{
    	return "Attempted to divide by 0! \n";
	}
};

int main()
{
    try    //try allows you to define a block of code to be tested for errors
    {
         int x,y;
         cout<<"\n Enter the 2 numbers :- ";
         cin>>x>>y;
         if(y==0)
         {
             myexception z;
             throw z;
         }
         else
         {
             cout<<"x/y= "<<x/y<<endl;
         }
    }
    catch(exception& e) //the catch statement allows you to define a block of code to be executed if an error occurs in the try block
    {
        cout<<e.what();
    }
    
}