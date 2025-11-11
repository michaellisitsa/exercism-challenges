#ifndef RESISTOR_COLOR_DUO_H
#define RESISTOR_COLOR_DUO_H

// Extended int types
#include <stdint.h>

typedef enum {
  BLACK = 0,
  BROWN,
  RED,
  ORANGE,
  YELLOW,
  GREEN,
  BLUE,
  VIOLET,
  GREY,
  WHITE,
} resistor_band_t;

uint16_t color_code(resistor_band_t colors[2]);

#endif
