It is easier to consider a pointer as a _data type_ just like integer, double, and float. It is a memory address. 

```c
int main{
	int age = 30;
	printf("Age's memory address is: %p\n", &age);
	return 0;
}
```

We can keep the memory address of the `age` variable by
```c
int * pAge = &age;
```

If we want to access to the data stored in the address then
```c
printf("%d", *pAge):
```

Equivalently, 
```c
printf("%d", *&age):
```