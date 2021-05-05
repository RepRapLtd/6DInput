/*

Read Hall sensors when prompted and return the voltages.


*/

int hallPin0 = A0;    // select the input pin for the potentiometer
int hallPin1 = A1;
int hallPin2 = A2;
int ledPin = 13;

void setup()
{
  pinMode(hallPin0, INPUT);
  pinMode(hallPin1, INPUT);
  pinMode(hallPin2, INPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}

void SendHallVoltages()
{
  int hallVoltage = analogRead(hallPin0);
  Serial.print(hallVoltage);
  Serial.print(" ");
  hallVoltage = analogRead(hallPin1);
  Serial.print(hallVoltage);
  //Serial.print(" ");
  //hallVoltage = analogRead(hallPin2);
  //Serial.print(hallVoltage);
  Serial.println();  
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
      SendHallVoltages();
    }
  }
}
