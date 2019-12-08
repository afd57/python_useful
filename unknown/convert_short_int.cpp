#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>
#include <string.h>

int
main (int argc, char **argv)
{
  char BYTE_0 = 0x64, BYTE_1 = 0x19;
  short int X_VALUE_LSB, X_VALUE_MSB;
  X_VALUE_LSB = BYTE_0;
  X_VALUE_LSB = X_VALUE_LSB & 0x00FF;
  
  X_VALUE_MSB = BYTE_1 << 8;
  X_VALUE_MSB = X_VALUE_MSB & 0xFF00;
  
  short int X_VALUE = X_VALUE_LSB + X_VALUE_MSB;
  printf ("%d\n", X_VALUE);
  
  // Data Bytes 2, 3 are 0xD8, 0xDC for -90.00 deg
  char BYTE_2 = 0xd8, BYTE_3 = 0xdc;
  short int Y_VALUE_LSB=0x0000, Y_VALUE_MSB=0X0000;
  
  
  Y_VALUE_LSB = BYTE_2;
  Y_VALUE_LSB = Y_VALUE_LSB & 0x00FF;
  Y_VALUE_MSB = BYTE_3 << 8 ;
  Y_VALUE_MSB = Y_VALUE_MSB & 0xFF00;
  
  short int Y_VALUE  = Y_VALUE_LSB + Y_VALUE_MSB;

  printf("\n");
  printf ("%d\n", Y_VALUE);

  return 0;
}

