#include <stdio.h>

int main(){
    char c;
    int answer,max,alpha[26],temp;
    for(int i=0; i<26; i++){
        alpha[i] = 0;
    }
    max = 0;
    scanf("%c",&c);
    while(c!='\n'){
        // printf("%c",c);
        if(c>='a' && c<='z'){
            alpha[(int)c-'a']++;
        }else{
            alpha[(int)c-'A']++;
        }

        scanf("%c",&c);
    }


    temp = 0;
    for(int i=0; i<26; i++){
        if(alpha[i]>max){
            max = alpha[i];
            answer = i;
            temp = 0;
        }else if(alpha[i]==max){
            temp = 1;
        }
    }
    if(temp==1){
        printf("?");
    }else{
        printf("%c",answer+'A');
    }

    return 0;
}