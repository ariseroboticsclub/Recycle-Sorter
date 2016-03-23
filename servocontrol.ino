#include <Servo.h>

Servo servo1, servo2, servo3; // Define servos
String command;
int cat = 90; //default angle when turned on
int move_pull = 0;
int move_fwd = 0;
int move_push = 190;
int move_bwd = 190;
void setup()
{
   servo1.attach(5); 
   servo2.attach(4);
   servo3.attach(6);
   servo1.write(cat);
   servo2.write(cat);
   servo3.write(cat);
   Serial.begin(9600);
}
void loop() {
  if (Serial.available()) {
     Serial.print("got data");
     command = Serial.readString();
  if (command == "1"){//plastic
   servo2.write(move_push);  //pushed
   delay(100);   
   servo1.write(move_pull);  //pulled back
   delay(2000);
   servo2.write(cat);  
   servo1.write(cat);  
   
  }
  else if (command =="2"){//aluminium
   servo2.write(move_pull);  //push in this case is this variable
   delay(100);   
   servo3.write(move_push);  //pull in this case is this variable
   delay(2000);
   servo2.write(cat);  
   servo3.write(cat);  
  }
  else if (command == "3"){//paper
   servo3.write(move_pull);  
   delay(100);   
   servo1.write(move_push);  
   delay(2000);
   servo3.write(cat);  
   servo1.write(cat);  
  }
  }
  else
    Serial.print("no data");
}

