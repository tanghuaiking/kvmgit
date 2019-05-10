//拆分测试。方法一，同时编译;方法二，函数调用，前部声明
//main.c

#include <stdio.h>
#include"king.h"
//extern int funa(int); //声明funa为外部函数
void main()
{
    int x=5,y;
    y=funa(x);
    printf("y=%d\n", y );
}
