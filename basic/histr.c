#include<stdio.h>
#include<string.h>

int main(void)
{
    char cArr[] = {'l', 'o', 'v', 'e','\0'};
    char sArr[] = "love";
    char *p = "love";
    int tArr[5];
    printf("tArr: %ld \n", sizeof(tArr));
    printf("tArr: %ld \n", sizeof(tArr)/sizeof(tArr[0]));

    printf("cArr: %ld \n", sizeof(cArr));
    printf("len of cArr: %ld \n", strlen(cArr));
    printf("%s \n", cArr);
    printf("--------------------------\n");

    printf("sArr: %ld \n", sizeof(sArr));
    printf("len of sArr: %ld \n", strlen(sArr));
    printf("%s \n", sArr);
    printf("--------------------------\n");

    printf("P: %ld \n",sizeof(p));
    printf("len of P: %ld \n", strlen(p));
    printf("%c \n", *p);
    printf("success\n");
    return 0;
}
