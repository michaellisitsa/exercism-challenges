#include "sublist.h"
#include <stdbool.h>
#include <string.h>

comparison_result_t check_lists(int *list_to_compare, int *base_list,
                                size_t list_to_compare_element_count,
                                size_t base_list_element_count) {
  // We need to compare contiguous memory over a slice of an array
  // Given the length of list "a"
  if (base_list_element_count == list_to_compare_element_count) {
    // Verify they contain exactly the same values
    int result = memcmp(list_to_compare, base_list, base_list_element_count);
    return result == 0 ? EQUAL : UNEQUAL;
  }
  if (list_to_compare_element_count == 0)
    return SUBLIST;
  if (base_list_element_count > list_to_compare_element_count) {
    int compare_index = 0;
    for (size_t i = 0;
         // <= because if lists are 3 and 5, we want to compare up to and
         // including the 3rd number [0, 1, 2, 3, 4], [2, 3, 4] should iterate
         // to index == 2
         i <= base_list_element_count - list_to_compare_element_count; i++) {
      if (list_to_compare[compare_index] == base_list[i]) {
        int result = memcmp(base_list + i, list_to_compare,
                            list_to_compare_element_count);
        if (result == 0) {
          return SUBLIST;
        }
      }
    }
  } else {
    // TODO: SUPERLIST
  }
  // 4. If we don't find it, we start with the next element in the list and
  // check whether it matches, from Step 0. This is less efficient than using
  // an aho corasick algorithm (trie) so you don't have to navigate back.
  return UNEQUAL;
}
