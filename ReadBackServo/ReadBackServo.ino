#include "Actuator.h"

#define POTPIN 8 //just some number for the pin
#define PWMPIN 9

Actuator a(POTPIN);

void setup() 
{
	a.attach(PWMPIN);
}

void loop()
{
	a.writeMicroseconds(1500); //write PWM period
	int pos = a.readPos();
}
