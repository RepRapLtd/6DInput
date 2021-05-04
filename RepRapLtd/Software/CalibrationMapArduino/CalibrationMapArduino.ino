/*

Read Hall sensors when prompted and return the voltages.


*/

int hallPin = A0;    // select the input pin for the potentiometer
int ledPin = 13;

void setup()
{
  pinMode(hallPin, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  char c;
  if(Serial.available() > 0)
  {
    while(Serial.available() > 0)
      c = Serial.read();
    if(c != '\n')
    {
      int hallVoltage = analogRead(hallPin);
      Serial.print(hallVoltage);
      Serial.print(" ");
      Serial.print(hallVoltage);
      digitalWrite(ledPin, 1);
      //delay(1000);
      digitalWrite(ledPin, 0);
    }
  }
}
