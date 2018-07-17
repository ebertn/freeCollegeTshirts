 #include<stdio.h>

int main(int argc, char** argv){
	if(argc != 2){
		printf("Not enough args");
	}

	FILE* colleges = fopen(argv[1], "r");
	FILE* new = fopen("formatted_colleges.csv", "w");

	int c = 0;
	int passed = 0;
	while((c = fgetc(colleges)) != EOF){
		if(c == '('){
			fputs(",admissions@", new);
			passed = 1;
			continue;
		} else if(c == ')'){
			passed = 0;
			continue;
		}
		
		if(!passed && c != ','){
			
			fputc(c, new);
		} else if(c != ' ' && c != ','){
			fputc(c, new);
		}
	}
	
	fclose(new);
	fclose(colleges);
	return 0;
}
