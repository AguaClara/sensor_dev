int analogPin = A0;
int val = 0;

void setup(){
  Serial.begin(9600);
  pinMode(7, OUTPUT);
}

void loop(){
  val = analogRead(analogPin);
  Serial.println(val);
  delay(200);
  digitalWrite(7, LOW);
  if(val > 150)
  {
    digitalWrite(7, HIGH);
  }
  else
  {
    digitalWrite(7, LOW);
  }
}
