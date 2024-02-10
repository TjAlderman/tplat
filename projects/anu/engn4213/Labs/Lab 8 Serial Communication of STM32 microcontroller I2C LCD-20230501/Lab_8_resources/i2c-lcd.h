#include "stm32f4xx_hal.h"

void lcd_init (uint16_t addr_7);   // initialize lcd

void lcd_send_cmd (char cmd, int i2c_frame_size);  // send command to the lcd

void lcd_send_data (char data);  // send data to the lcd

void lcd_send_string (char *str);  // send string to the lcd


void lcd_clear (void);
