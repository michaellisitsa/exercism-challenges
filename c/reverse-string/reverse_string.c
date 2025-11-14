#include "reverse_string.h"
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char *reverse(const char *value) {
  uint8_t length = strlen(value);
  char *newValue;
  newValue = (char *)malloc(length * sizeof(char) + 1);
  for (int i = 0; i < length; i++) {
    newValue[i] = value[length - 1 - i];
  }
  newValue[length] = '\0';
  return newValue;
}
