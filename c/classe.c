#include <stdio.h>
#define max 100

typedef struct {
	char nome[30];
	char cognome[30];
	int media;
} studente;

void carica_classe(studente classe[], int num) {
	int i;
	for(i=0; i<num; i++) {
		printf("Studente n. %d (nome cognome media): ", i+1);
		scanf("%s %s %d", &(classe[i].nome), (classe[i].cognome), &(classe[i].media));
	}
}

void stampa_classe(studente classe[], int num) {
	int i;
	for(i=0; i<num; i++) {
		printf("Studente n. %d\n\tNome: %s\n\tCognome: %s\n\tMedia: %d\n", i+1, classe[i].nome, classe[i].cognome, classe[i].media);
	}
}

int compare(const studente *a, const studente *b) {
	if (a->media < b->media) return -1;
	if (a->media == b->media) return 0;
	if (a->media > b->media) return 1;
}

void ordina_classe(studente classe[], int num) {
	qsort(classe, num, sizeof(studente), (void *)compare);
}

int main(void) {
	studente classe[max];
	int num;

	printf("Quanti studenti ci sono nella classe? ");
	scanf("%d", &num);
	
	carica_classe(&classe[0], num);
	printf("\n---CLASSE NON ORDINATA---\n\n");
	stampa_classe(&classe[0], num);
	
	printf("\n---CLASSE ORDINATA---\n\n");
	ordina_classe(&classe[0], num);
	stampa_classe(&classe[0], num);
	
	return 0;
}
