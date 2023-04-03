#include <stdio.h>

int main()
{
    int take, untake;
    int num = 0, max = 0 ;
    for(int i = 0 ; i<4;i++)
    {
        scanf("%d %d",&untake,&take);
        num = num + take - untake;
        if(num>max)
            max = num;
    }
    
    printf("%d",max);
}