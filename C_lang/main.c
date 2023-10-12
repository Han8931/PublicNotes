#include <stdio.h>
#include <stdlib.h>

/*Prototype*/
double cube(double num);

int main()
{
	int age = 30;
	printf("Your age is %i\n", age);
	printf("Age's memory address is %p\n", &age);

	int * pAge = &age;
	printf("Age's memory address is %p\n", pAge);

	printf("What's the age? %d\n", *pAge);
	printf("What's the age? %d\n", *&age);
	return 0;
}

double cube(double num){
	return num*num*num;
}
