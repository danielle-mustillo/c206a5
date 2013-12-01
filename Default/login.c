#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cipher.c"

int verify(char *user , char *pass){

	char *parsed_user;
	char *parsed_pass;
	char buffer[200];	
	// create new file pointer
	FILE *file_ptr;
	file_ptr = fopen("password.csv", "rt");
	//if password.csv doesn't exist,return error
	if(file_ptr==NULL){
		return 1;
	}
	else{
		while(fgets(buffer, 200, file_ptr) != NULL){
		 	decrypt(buffer);
		 	parsed_user = strtok (buffer, ",");
		 	parsed_pass = strtok (NULL,",");
		 	if ((strcmp(user,parsed_user)) == 0 && (strcmp(pass,parsed_pass)) == 0){
		 		fclose(file_ptr);
		 		return 0;
		 	}
		}
		fclose(file_ptr);
		return 1;	 	
	}
}

void print_error(){
	printf("%s%c%c\n","Content-Type:text/html",13,10);
	printf("<HTML><BODY>\n");
	printf("<h1 align=\"center\"> Wrong Username/Password ");
	printf("<P><a href=\"http://www.cs.mcgill.ca/~hzhao28/ass5/index.html\"> Back to Welcome Page </a> <P>\n");
	printf("</BODY></HTML>\n");

}


void main(void){
	
	char Buffer[256] = {0};
	char username[256] = {0};
	char password[256] = {0};
	if(getenv("CONTENT_LENGTH") == NULL) {
		print_error();
		exit(1);
	}
	else{

		int input_length = (int) (strtol(getenv("CONTENT_LENGTH"),NULL,10));
		//copy the input into an array
		fgets(Buffer,input_length + 1,stdin);
		//parse out the username and password
		strtok(Buffer,"=");
		strcpy(username,strtok(NULL,"&"));
		strtok(NULL,"=");
	  	strcpy(password,strtok(NULL,"&"));
	  	//check user/pass against the .csv
	 	if(verify(username,password)==1){
	 		//failed
			print_error();
		}
		//sucess
		else if(verify(username,password) == 0  ){
			printf("Location:http://www.cs.mcgill.ca/~dmusti/comp206/room.html\n\n");
		}
	}
}


