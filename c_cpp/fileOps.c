#include <stdio.h>
#include <string.h>

int main()
{
    FILE *fp;

    // 以ascii码查看内存 -exec x/32c data
    char data[50];
    // 创建或打开文件
    printf("Opening the file test.c in write mode");
    fp = fopen("test.c", "w"); // r 不会创建, w会创建文件， 如果文件创建失败，需要fp不为空的情况再释放!
    if (fp == NULL)
    {
        printf("Could not open file test.c");
        return 1;
    }
    printf("\n Enter some text from keyboard” \
             “ to write in the file test.c");
    // 获取用户输入
    while (strlen(gets(data)) > 0)
    {
        // writing in the file
        fputs(data, fp);
        fputs("\n", fp);
    }
    // 关闭文件
    printf("Closing the file test.c");
    if(fp != NULL){
        fp = NULL;
        fclose(fp);
    }
    
    return 0;
}