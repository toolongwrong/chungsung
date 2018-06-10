#include<stdio.h>
#include<string.h>
int main(int argc,char **argv)
{
    if(argc<2)
        return;
    
    FILE *open_file;
    char b[300];
    int count;
    count = 0;
    char c[10];
    strcpy(c,argv[1]);
    strcat(c,".txt");
    printf("%s",c);
   
    open_file = fopen(c,"r");
    while((feof(open_file)== 0))
    {
        count++;
        fgets(b,sizeof(b),open_file);
    }
    fclose(open_file);
    int value;
    value= 0;
    if(count <400)
    {
        value = 50;
    }
    else if(count <800)
    {
        value = 200;
    }
    else if(count <1000)
        value = 300;
    else if(count <1200)
        value = 500;
    else if(count <1700)
        value = 600;
    else if(count >1700)
        value = 800;
    open_file = fopen("tensor.txt","a");
    fprintf(open_file,"%s %d %d\n",argv[1],count,value);
    fclose(open_file);
}
