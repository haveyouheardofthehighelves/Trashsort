char incomingByte = 0; 
String message = "";
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    // Read the incoming byte
    incomingByte = Serial.read();
    message += incomingByte;
    if(message.length()>1){
      if(message[message.length()-1]=='$'||message[message.length()-1]=='*'){
        Serial.println(message);
         message = "";        
      }
    }
    }

}
