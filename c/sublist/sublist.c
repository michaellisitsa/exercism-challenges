#include "sublist.h"
#include <stdbool.h>
#include <string.h>

comparison_result_t check_lists(int *list_to_compare, int *base_list,
                                size_t list_to_compare_element_count,
                                size_t base_list_element_count) {
  if (base_list_element_count == list_to_compare_element_count) {
    return memcmp(base_list, list_to_compare,
                  base_list_element_count * sizeof(int)) == 0
               ? EQUAL
               : UNEQUAL;
  } else if (list_to_compare_element_count == 0) {
    return SUBLIST;
  } else if (base_list_element_count == 0) {
    return SUPERLIST;
  } else if (base_list_element_count > list_to_compare_element_count) {
    // SUBLIST
    for (size_t i = 0;
         // Example: [0, 1, 2, 3, 4], [2, 3, 4] should iterate to index == 2
         i <= base_list_element_count - list_to_compare_element_count; i++) {
      if (list_to_compare[0] == base_list[i] &&
          // corasick algorithm (trie) would prevent O(N2)
          memcmp(base_list + i, list_to_compare,
                 list_to_compare_element_count * sizeof(int)) == 0) {
        return SUBLIST;
      }
    }
  } else {
    // SUPERLIST
    for (size_t i = 0;
         i <= list_to_compare_element_count - base_list_element_count; i++) {
      if (base_list[0] == list_to_compare[i] &&
          memcmp(base_list, list_to_compare + i,
                 base_list_element_count * sizeof(int)) == 0) {
        return SUPERLIST;
      }
    }
  }
  return UNEQUAL;
}
