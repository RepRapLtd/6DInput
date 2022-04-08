/*

Read Hall sensors when prompted and return the voltages.


*/

#define SENSOR_COUNT 1

int hallPins[6] = {A0, A1, A2, A3, A4, A5}; 

int ledPin = 13;

void setup()
{
  for(int i = 0; i < SENSOR_COUNT; i++)
  {
    pinMode(hallPins[i], INPUT);
  }
  pinMode(ledPin, OUTPUT);
  Serial.begin(115200);
}


void loop()
{
  for(int i = 0; i < SENSOR_COUNT; i++)
  {
    int hallReading = analogRead(hallPins[i]);
    Serial.print("Hall ");
    Serial.print(i);
    Serial.print(" reading: ");
    Serial.print(hallReading);
    Serial.print(", (");
    float v = (float)hallReading*5.0/1023.0;
    Serial.print(v);
    Serial.println(" volts).");
  }
  
  delay(500);
}  
