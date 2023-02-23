#include <stdio.h>
typedef char literal[256];
int main(){
/*-------Variaveis temporarias---------*/
int T1;
int T2;
int T3;
int T4;
int T5;
/*------------------------------*/
literal A;
int B,D;
double C;
printf("Digite B");
scanf("%d", &B);
printf("Digite A:");
scanf("%s", &A);
T1 = B > 2;
if(T1)
{
 T2 = B <= 4;
if(T2)
{
 printf("B esta entre 2 e 4");
}
}
T3 = B + 1;
B = T3;
T4 = B + 2;
B = T4;
T5 = B + 3;
B = T5;
D = B;
C = 5.0;
printf("\nB=\n");
printf("%d",D);
printf("\n");
printf("%lf",C);
printf("\n");
printf("%s",A);
return 0;
}