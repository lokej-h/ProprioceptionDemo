#include <Servo.h>

class Actuator : public Servo
{
  private:
    unsigned int potPin;
  public:
    Actuator(int potPin) : Servo()
    {
      this->potPin = potPin;
    }
    int readPos()
    {
      return map(analogRead(potPin), 0, 1023, 0, 1000); // reads the pot and reads the position as a percentage * 10
    }
    
};
