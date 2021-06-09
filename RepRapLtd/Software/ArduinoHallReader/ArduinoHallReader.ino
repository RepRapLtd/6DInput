/*

Read (some) Hall sensors when prompted and return the voltages.

RepRap Ltd
https://reprapltd.com

Adrian Bowyer
9 June 2021

Licence: GPL


*/


int hallPin[6] = {A0, A1, A2, A3, A4, A5};
const int pins = 6;
int ledPin = 13;

void setup()
{
  for(int p = 0; p < pins; p++)
  {
    pinMode(hallPin[p], INPUT);
  }
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void SendHallVoltages(int number)
{
  int hallVoltage;
  
  if(number <= 0)
    number = 1;
  if(number > pins)
    number = pins;
  
  for(int p = 0; p < number; p++)
  {
    hallVoltage = analogRead(hallPin[p]);
    Serial.print(hallVoltage);
    Serial.print(" ");
  }
  Serial.println();  
}

void loop()
{
  int number;
  if(Serial.available() > 0)
  {
    number = Serial.read();
    if(number != '\n')
    {
      number = number - '0';
      SendHallVoltages(number);
    }
    while(Serial.available() > 0)
      number = Serial.read();
  }
}
