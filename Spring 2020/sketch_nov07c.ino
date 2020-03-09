long analogPin0 = A0;
int analogPin1 = A1;
int val_scattered = 0;
int val_transmitted = 0;
int sum = 0;
int sum_2 = 0;
int avg = 0;
int iter = 0;

void setup(){
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  
}

void loop(){
  if(iter != 10)
  {
  Serial.println("Scattered:     Transmitted:");
  }
  while(iter < 10){
    val_scattered = analogRead(analogPin0);
    val_transmitted = analogRead(analogPin1);
    Serial.println("          "+(String)val_scattered+"              "+(String)val_transmitted);
    sum += val_scattered;
    sum_2 += val_transmitted;
    delay(200);
    iter++;
  }
  if(iter < 10){
  avg = sum / 10;
  Serial.println("Scattered average: " + avg);
  avg = sum_2 / 10;
  Serial.println("Transmitted average: " + avg);
  }
}
