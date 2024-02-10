
/** include this file in the src folder **/

#include "i2c-lcd.h"
#include "main.h"
extern I2C_HandleTypeDef hi2c1;  // change your handler here accordingly

#define SLAVE_ADDRESS_LCD 0x27 // change this according to your setup


uint16_t addr_8=SLAVE_ADDRESS_LCD;


void lcd_send_cmd (char cmd,int i2c_frame_size)
{

		uint8_t i2c_frame_data[4];

		i2c_frame_data[0] = (cmd & 0xF0) | 0x0c;
		i2c_frame_data[1] = i2c_frame_data[0] & 0xFB;

		i2c_frame_data[2] = ((cmd << 4) & 0xF0) | 0x0c;
		i2c_frame_data[3] = i2c_frame_data[2] & 0xFB;

		// HAL transmits i2c_frame_data[0],[1], ... , i2c_frame_data[i2c_frame_size-1]
		//Please write your own code here
		HAL_I2C_Master_Transmit(&hi2c1, addr_8,(uint8_t *) i2c_frame_data, sizeof(i2c_frame_data), 10000);

		HAL_Delay(1);

}

void lcd_send_data (char data)
{
	char data_u, data_l;
	uint8_t i2c_frame_data[4];
	data_u = (data&0xf0);
	data_l = ((data<<4)&0xf0);
	i2c_frame_data[0] = data_u|0x0D;  //en=1, rs=0
	i2c_frame_data[1] = data_u|0x09;  //en=0, rs=0
	i2c_frame_data[2] = data_l|0x0D;  //en=1, rs=0
	i2c_frame_data[3] = data_l|0x09;  //en=0, rs=0
	// HAL transmits i2c_frame_data[0],[1], ... , i2c_frame_data[i2c_frame_size-1]
		//Please write your own code here
	HAL_I2C_Master_Transmit(&hi2c1, addr_8, (uint8_t *) i2c_frame_data, sizeof(i2c_frame_data), 10000);

	HAL_Delay(1);
}

void lcd_clear (void)  // clear display
{
	//send command to clear the display
	//Please write your own code here
	lcd_send_cmd(0x01,4);
	HAL_Delay(500);
	
	HAL_Delay(1);
}

void lcd_init (uint16_t addr_7)
{

	addr_8=addr_7<<1;
    // 4-bit mode initialisation
	//Please write your own code here
	HAL_Delay(50);
	lcd_send_cmd(0x30,4);
	HAL_Delay(5);
	lcd_send_cmd(0x30,4);
	HAL_Delay(1);
	lcd_send_cmd(0x30,4);
	HAL_Delay(10);
	lcd_send_cmd(0x20,4);
	HAL_Delay(10);
	lcd_send_cmd(0x28,4);
	HAL_Delay(1);
   // display initialisation
  //Please write your own code here
	lcd_send_cmd(0x08,4);
	HAL_Delay(10);
	lcd_send_cmd(0x01,4);
	HAL_Delay(10);
	lcd_send_cmd(0x06,4);
	HAL_Delay(10);
	lcd_send_cmd(0x0C,4);
	HAL_Delay(20);



}

void lcd_send_string (char *str)
{
//Please write your own code here
	uint8_t i=0;
	while(str[i]!=0){
		lcd_send_data(str[i]);
		i++;
		HAL_Delay(100);
	}
//	for (uint8_t i=0; i<12; i++) {
//		lcd_send_data(str[i]);
//		HAL_Delay(1);
//	}
}
