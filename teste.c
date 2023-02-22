#include <stdio.h>
typedef char literal[256];
int main(){
/*-------Variaveis temporarias---------*/
int T1;
double T2;
/*------------------------------*/
int idade;
int a,b;
double peso;
double dobro;
literal nome;
printf("Digite a sua idade: \n");
scanf("%d", &idade);
printf("Digite seu nome: \n");
scanf("%s", &nome);
printf("Digite seu peso: \n");
scanf("%lf", &peso);
T1 = idade >= 18;
if(T1)
{
 printf("%s\n",nome);
printf(" é maior de idade!\n");
}
T2 = peso * 2;
dobro = T2;
printf("o dobro do peso é:\n");
printf("%lf\n",dobro);
return 0;
}