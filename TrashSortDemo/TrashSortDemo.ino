#include <Servo.h>
#include <LiquidCrystal.h> 
Servo myservo;
int servopin = 9; 
int ir = A0; 
int cw = 8;
int ccw = 10;
int last_angle = 0;
int Contrast=75;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
void setup() {
  analogWrite(6,Contrast);
  lcd.begin(16, 2);
  pinMode(servopin, OUTPUT); 
  pinMode(ir, INPUT); 
  pinMode(cw, OUTPUT); 
  pinMode(ccw, OUTPUT); 
  myservo.attach(servopin); 
  myservo.write(last_angle); 
  digitalWrite(ccw, LOW); 
  Serial.begin(9600); 
  // put your setup code here, to run once:
}

void loop() {
  lcd.setCursor(0, 0);
  lcd.print("HELLO WORLD!");
   
  lcd.setCursor(0, 1);
  lcd.print("fuck off :]");
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
    digitalWrite(cw, HIGH); 
    delay(500);
    digitalWrite(cw, LOW); 
  }
}
  // put your main code here, to run repeatedly:
