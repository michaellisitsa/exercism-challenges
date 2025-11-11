#include "pangram.h"
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

bool is_pangram(const char *sentence) {
  if (sentence == NULL) {
    return false;
  } else if (sentence[0] == '\0') {
    // This statement isn't even needed as you can just loop over the zero
    // length item
    return false;
  }
  // Create an array of 26 length
  // Fill the array with zeros
  int charTracker[26] = {0};
  // For each letter, get the item at the array slot and change to 1.
  for (uint32_t i = 0; i < strlen(sentence); i++) {
    int asciiValue;
    asciiValue = sentence[i];

    // Stdlib alsa has an isalpha, and a tolower
    if (asciiValue >= 97 && asciiValue <= 122) {
      charTracker[asciiValue - 97] = 1;
    } else if (asciiValue >= 65 && asciiValue <= 90) {
      charTracker[asciiValue - 65] = 1;
    }
  }
  int count = 0;
  // Possible optimisation: As soon as we encounter a zero, we can return false.
  // see https://exercism.org/tracks/c/exercises/pangram/solutions/archanarawat
  for (int i = 0; i < 26; i++) {
    // Iterate over the array counting to see if adds up to 26.
    count += charTracker[i];
  }
  if (count == 26)
    return true;
  return false;
}
