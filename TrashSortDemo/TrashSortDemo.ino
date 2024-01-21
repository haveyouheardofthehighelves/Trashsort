#include <Servo.h>
Servo myservo;
int servopin = 9; 
int ir = A0; 
int cw = 8;
int ccw = 10;
int last_angle = 0;
void setup() {
  pinMode(servopin, OUTPUT); 
  pinMode(ir, INPUT); 
  pinMode(cw, OUTPUT); 
  pinMode(ccw, OUTPUT); 
  myservo.attach(servopin); 
  myservo.write(last_angle); 
  Serial.begin(9600); 
  // put your setup code here, to run once:

}

void loop() {
  int value = analogRead(ir); 
  Serial.println(value); 
  if (value >= 250){ 
    if(last_angle == 0){
      myservo.write(180);
      last_angle = 180;   
    }else{
      myservo.write(0); 
      last_angle = 0; 
    }
    delay(1500); 
    digitalWrite(3, HIGH); 
    delay(500);
    digitalWrite(3, LOW); 
  }
  // put your main code here, to run repeatedly:

}
