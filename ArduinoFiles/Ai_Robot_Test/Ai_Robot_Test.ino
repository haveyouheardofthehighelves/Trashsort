#include <Servo.h>
#include <LiquidCrystal.h> 
Servo myservo;
int servopin = 9;
int ir = A0;
int cw = 8;
int ccw = 10;
int last_angle = 0;
int x = cw; int y = ccw;
String hello = ""; 
int Contrast = 75;
bool nobject = false; 
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 
void setup() {
  analogWrite(6,Contrast);
  lcd.begin(16, 2);
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
  digitalWrite(x, LOW); 
}

void loop() {
  
  int value = analogRead(ir);
  if (value >= 250){ 
    nobject = false;
    if(Serial.available() > 0){
      char c = Serial.read(); 
      if(c == '!' || c == '-'){
        if( c == '!'){
          myservo.write(0); 
        }
        if(c=='-'){
         myservo.write(180);
        }    
        delay(250); 
        digitalWrite(8, HIGH);
        digitalWrite(10, LOW); 
        delay(500); 
        digitalWrite(8, LOW);  
      }
      if(c == '('){
        digitalWrite(10, HIGH); 
        digitalWrite(8, LOW); 
        delay(1000); 
        digitalWrite(10, LOW); 
      }
      if (c == '*') {
        lcd.setCursor(0, 0);
        lcd.clear();
        lcd.print(hello);
    } else if (c == '#') {
        lcd.setCursor(0, 1);
        lcd.print(hello);
        Serial.println(hello); 
    } else {
      hello += c; 
    }

    // Reset the 'hello' string after printing on both lines
    if (c == '#' || c == '*') {
      hello = ""; 
    }
  }
      
   }else{
     if(!nobject){
     lcd.clear(); 
     lcd.setCursor(0, 0);
     lcd.print("no object");
     nobject = true;
     lcd.setCursor(0, 1);
     lcd.print("present");
     while (Serial.available() >0 ) {
              Serial.read();
           }
   }
  // put your main code here, to run repeatedly:

}
}
