#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <math.h>
//SezinGümüş 150113841
//ErhanGüngör 150113066
struct city{
	char city_name[1000000];
	int x;
	int y;
	int a;		//if city is visited a=1 , else a=0
	struct city *nextCity;
};

void ReadFromFile();	//Read inputs from txt file
int insert(struct city ** header, char *name, int x, int y);
int calculateDistance(struct city *city1, struct city *city2);
int calculateNumber();	//Calculate number of cities
int createAdjacencyMatrix(int ** matrix, int n);
void displayMatrix(int ** matrix, int n);
struct city* FindMedium(int n);	//Find the median of all cities
struct city* FindCity(int n);	//Find nth city
void FindPath(int ** matrix, struct city *medium, int n);	//Find the closest path
void displayCity(struct city *show);	//Display a city
void WriteToFile();		//Write output to txt file

struct city *header = NULL;		//root of cities(taken from input)
struct city *header1 = NULL;	//root of cities(output)

int sum = 0;	//Total received path
FILE *file;

int main(){
	struct city *medium;
	ReadFromFile();
	int n = calculateNumber();

	int ** matrix; //Adjancency Matrix
	int i;
	matrix = malloc(n * sizeof(int*));
	for(i=0; i<n; i++)
		matrix[i] = malloc(n * sizeof(int));

	createAdjacencyMatrix(matrix,n);
	FindPath(matrix,medium,n);
	WriteToFile();
	displayMatrix(matrix,n);
	//display(header);
	//displayCity(header);
}

void FindPath(int ** matrix, struct city * medium, int n){
	struct city *temp = header;
	int i=0;
	insert(&header1,temp->city_name,temp->x,temp->y);
	//displayCity(temp);
	int d = 99999999;
	int k,j,nextCity=0;
	temp->a = 1;	//City is visited

	//Find the closest city
	for(k=0; k<n-1; k++){
		for(j=0; j<n; j++){
			if(d > matrix[i][j] && i != j && FindCity(j)->a == 0){
				d = matrix[i][j];
				nextCity = j;
			}
		}
		sum+=d;	//Add received path to total
		d = 99999999;
		//Find the next city
		i = nextCity;
		temp = FindCity(nextCity);
		//printf("%s \n",temp->city_name,temp->x,temp->y);
		temp->a = 1;	//City is visited
		if(k == n-2)
			sum+=calculateDistance(header1,temp);	//Add distance between last city and start point
		insert(&header1,temp->city_name, temp->x, temp->y);
	}
}

struct city * FindCity(int n){
	struct city *temp = header;
	int i=0;
	while(temp != NULL && i<n){
		temp = temp->nextCity;
		i++;
	}
	return temp;
}

void ReadFromFile(){
	file = fopen("test1.txt" , "r");
	int temp_x = 0;
	int temp_y = 0;
	char temp_name[1000000];
	if(file){
		char line[300];
		while(fgets(line, sizeof line, file)){
			char *temp1;
			char *temp2;
			temp1 = strtok(line, "\n");
			temp2 = strtok(temp1, " ");
			strcpy(temp_name,temp1);

			temp2 = strtok(NULL, " ");

			temp_x = atoi(temp2);
			temp2 = strtok(NULL, " ");

			temp_y = atoi(temp2);
		//	printf("%s - %d - %d \n",temp_name,temp_x,temp_y);

			insert(&header,temp_name,temp_x,temp_y);
		}
	}
	fclose(file);
}

void WriteToFile(){
	struct city *temp = header1;
	file = fopen("output.txt" , "w");
	if(file){
		fprintf(file,"%d\n",sum);
		while(temp){
			fprintf(file,"%s\n",temp->city_name);
			temp = temp->nextCity;
		}
	}
	fclose(file);
}

struct city* FindMedium(int n){
	//Find the median of all cities
	char* name= "temp";
	double tempdiff;
	double diff = 9999999;
	struct city *temp,*newNode,*medium;
	temp = header;
	double sumx = 0, sumy = 0;
	while(temp){
		sumx = sumx + temp->x;
		sumy = sumy + temp->y;
		temp = temp->nextCity;
	}

	sumx = sumx/n;
	sumy = sumy/n;

	newNode=(struct city*)malloc(sizeof(struct city));
	strcpy(newNode->city_name,name);
	newNode->nextCity=NULL;
	newNode->x=sumx;
	newNode->y=sumy;
	newNode->a=0;
	temp = header;

	while(temp){
		tempdiff = calculateDistance(temp,newNode);
		if(tempdiff < diff){
			diff = tempdiff;
			medium = temp;
		}
		temp = temp->nextCity;
	}
	return medium;
}

int createAdjacencyMatrix(int ** matrix, int n){
	struct city *temp1 = NULL;
	struct city *temp2 = NULL;
	temp1 = header;
	temp2 = header;
	int i,j;
	for(i=0;i<n ; i++){
		for(j=0; j<n; j++){
			matrix[i][j] = calculateDistance(temp1,temp2);
			temp2 = temp2->nextCity;
		}
		temp1 = temp1->nextCity;
		temp2 = header;
	}
}

int calculateNumber(){
	struct city *temp = header;
	int n = 0;
	while(temp){
		n++;
		temp = temp->nextCity;
	}
	return n;
}
int calculateDistance(struct city *city1, struct city *city2){
	//Calculate distance betweeen 2 cities and return closest integer
	double temp;
	temp = sqrt(pow(city1->x - city2->x,2) + pow(city1->y - city2->y,2));
	int distance = 0;
	int y = (int)(temp);
	int z = y*100 + 50;
	int a = (int)(temp*100);
	if(z < a)
		distance = y+1;
	else
		distance = y;
	//printf("%s - %s = %d\n",city1->city_name,city2->city_name,distance);
	return distance;
}

int insert(struct city ** header, char *name, int x, int y){

	struct city *newNode, *temp;

	// create node to insert and assign values to its fields
	newNode=(struct city*)malloc(sizeof(struct city));
	strcpy(newNode->city_name,name);
	newNode->nextCity=NULL;
	newNode->x=x;
	newNode->y=y;
	newNode->a=0;
	// if LL empty
	if (*header == NULL)
		*header=newNode;
	// if LL not empty
	else {
		temp=*header;

		while (temp->nextCity != NULL ){
			temp=temp->nextCity;
		}
        temp->nextCity = newNode;
	}

	return 1;

}

void displayMatrix(int ** matrix, int n){
	//Display the matrix
	int i,j;
	i=0;
	while(i<n){
		printf("  %d  ",i);
		i++;
	}
	printf("\n");
	i=0;
	while(i<n){
		printf("----");
		i++;
	}
	printf("\n");
	i=0;

	for(i=0; i<n; i++){
		printf("%d|",i);
		for(j=0; j<n; j++){
			printf("%d,",matrix[i][j]);
		}
		printf("\n\n");
	}
}

//display a linked list(all cities)
void display(struct city *show){
	while(show){
		printf("%s -> (%d,%d)\n",show->city_name,show->x,show->y);
		show=show->nextCity;
	}
}

//display a city(one node in linked list)
void displayCity(struct city *show){
	printf("City Name -> Coordinates\n");
	printf("------------------------\n");
	printf("%s -> (%d,%d)\n",show->city_name,show->x,show->y);
}

