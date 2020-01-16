#include <Servo.h>

class ServoReadBack : public Servo
{
  private:
    unsigned int potPin;
  public:
    ServoReadBack(int potPin) : Servo()
    {
      this->potPin = potPin;
    }
    void readPos()
    {
      return map(analogRead(potPin), 0, 1023, 0, 1000); // reads the pot and reads the position as a percentage * 10
    }
    
};
