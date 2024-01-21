#include <Servo.h>
Servo myservo;
int servopin = 9;
int ir = A0;
int cw = 8;
int ccw = 10;
int last_angle = 0;
int x = cw; int y = ccw;
String hello = ""; 
void setup() {
  pinMode(servopin, OUTPUT);
  pinMode(ir, INPUT);
  pinMode(cw, OUTPUT);
  pinMode(ccw, OUTPUT);
  myservo.attach(servopin);
  myservo.write(0);
  Serial.begin(9600);
  // put your setup code here, to run once:

}

void Rotate(int x, int y){ 
  digitalWrite(x, HIGH); 
  digitalWrite(y, LOW); 
  delay(500); 
  digitalWrite(x, LOW); 
}

void loop() {
  
  int value = analogRead(ir);
  Serial.println(value);
  if (value >= 250){ 
    delay(1500); 
    Serial.println('.');
    for(int i = 0; i<3; i++){
      if(Serial.available()>0){
        char c = Serial.read(); 
        if(c == '('){
          myservo.write(180); 
        }
        else if(c == ')'){
          myservo.write(0); 
        }
        else if(c == '%'){
          x = ccw;
          y = cw; 
        }
        else if(c=='$'){
          x = cw;
          y = ccw; 
        }else{
        hello += c;
      }
      }
   }
   Rotate(x,y); 
  }
  // put your main code here, to run repeatedly:

}
