#include<stdio.h>
int swap(int num1, int num2){
    printf("Swapping two numbers");
    num1=num1+num2;
    num2=num1-num2;
    num1=num1+num2;
    return 1;
}

int main(){
    int num1, num2;
    printf("Enter the numbers to be swapped:");
    scanf("%d %d", &num1, &num2);
    printf("The swapped numbers are:\n");
    swap(num1, num2);
    return 1;
}