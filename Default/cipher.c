//Han Yang Zhao
//260534081

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

void encrypt( char *input){

	int inputascii;
	int modascii;
 	int encryptnum = 13;

	for (int i = 0 ; i < strlen(input); i++){
        if( input[i] != '\0' && input[i] != '\n'){
		    inputascii = input[i];  
            modascii = inputascii + encryptnum ;

            //warps the letter around to a if the letter becomes bigger than z
            if(modascii > 'z' && (inputascii >= 'a' && inputascii <= 'z' )){
        	   modascii = modascii - 'z' + 'a' - 1;
            }
            //warps the letter around to A if the letter becomes bigger than Z
            else if (modascii >'Z' && (inputascii >= 'A' && inputascii <= 'Z')){
                modascii = modascii - 'Z' + 'A' - 1;
            }
            input[i] = modascii;
        }
    }
}


void decrypt ( char *input){

	int inputascii;
    int modascii;
    int decryptnum = 13;
  
    for(int j = 0 ; j < strlen(input); j++){
        if( input[j] != '\0' && input[j] != '\n'){
            inputascii = input[j]; 
           	 modascii = inputascii - decryptnum;

            //warps the letter around to z if the letter becomes smaller than a
            if(modascii < 'a' && (inputascii >= 'a' && inputascii <= 'z' )){
                modascii = modascii + 'z' - 'a' + 1;
            }

            //warps the letter around to Z if the letter becomes smaller than A
            else if (modascii <'A' && (inputascii >= 'A' && inputascii <= 'Z')){
                modascii = modascii + 'Z' - 'A' + 1;
            }
            input[j] = modascii;
        }        
    }
}
	