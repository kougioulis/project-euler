//Project Euler Problem 22

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define FILE_SIZE 64000 /* max size in bytes */
#define MAX_NAMES 5163 /* total names in the file */

int compare(const void *x, const void *y) {
  return strcmp(*(char * const *)x, *(char * const *)y);
}

int main(int argc, char *argv[]) {

  FILE* names_file;

  names_file = fopen(argv[1], "r");

  char input_buffer[FILE_SIZE] = { '\0' }; /* buffer for file contents */

  if (names_file == NULL) {
    printf("Couldn't open the file, bye! \n");
    return EXIT_FAILURE;
  }

  fread(input_buffer, 1, FILE_SIZE, names_file);

  fclose(names_file);

  char *names[MAX_NAMES];

  // Parse the input_buffer:
  int count = 0;
  char *name;
  name = strtok(input_buffer, ",");

  do {
    int name_len = strlen(name);

    names[count] = (char *) malloc((name_len + 1) * sizeof(char));

    if (names[count] == NULL) {
      printf("Malloc failed, bye!");
      return EXIT_FAILURE;
    }

    // Copy the name into the names array:
    strcpy(names[count++], name);

  } while (name = strtok(NULL, ","));

  // Sort the names using quicksort
  qsort(names, count, sizeof(char *), compare);

  int total_score = 0;

  for (int i = 0; i < count; i++) {
    int name_score = 0;

    for (int j = 0; j < strlen(names[i]); j++) {
      name_score += (names[i][j] - 'A' + 1);
    }

    total_score += name_score * (i + 1);
  }

  printf("%d\n", total_score);

  for (int i = 0; i < count; i++) {
    free(names[i]);
  }

  return EXIT_SUCCESS;
}

