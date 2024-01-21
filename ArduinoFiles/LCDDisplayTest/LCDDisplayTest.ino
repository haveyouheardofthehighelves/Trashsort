#include <LiquidCrystal.h> 

int Contrast = 75;
String hello = "";
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 

void setup() {
  analogWrite(6,Contrast);
  lcd.begin(16, 2);
  Serial.begin(9600); 
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read(); 
    if (c == '*') {
      lcd.setCursor(0, 0);
      lcd.clear();
      lcd.print(hello);
      Serial.println(hello); 
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
}
