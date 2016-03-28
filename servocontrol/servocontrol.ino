#include <Servo.h>

Servo servo1, servo2, servo3; // Define servos
String command;
int cat = 90; //default angle when turned on
int move_pull = 0;
int move_fwd = 0;
int move_push = 190;
int move_bwd = 190;

const int button1=5;
const int button2=6;
const int button3=7;

void setup()
{
  servo1.attach(3); 
  servo2.attach(2);
  servo3.attach(4);
  servo1.write(cat);
  servo2.write(cat);
  servo3.write(cat);
  Serial.begin(9600);

  pinMode(button1,INPUT);
  pinMode(button2,INPUT);
  pinMode(button3,INPUT);
}
void loop() {
  
  //if (Serial.available()) {
   // Serial.print("got data");
    //command = Serial.readString();
     
/*   
  if(digitalRead(button1)==HIGH){
    command="1";
    Serial.println("button1");
  }
  if(digitalRead(button2)==HIGH){
    command="2";
    Serial.println("button2");
  }
  if(digitalRead(button3)==HIGH){
    command="3";
    Serial.println("button3");
  }
  */

  //command=="1"
  if (digitalRead(button1)==HIGH){//plastic
  Serial.println("button1");
   servo2.write(move_push);  //pushed
   delay(100);   
   servo1.write(move_pull);  //pulled back
   delay(2000);
   servo2.write(cat);  
   servo1.write(cat);  
  }


  else if (digitalRead(button2)==HIGH){//aluminium
  Serial.println("button2");
   servo2.write(move_pull);  //push in this case is this variable
   delay(100);   
   servo3.write(move_push);  //pull in this case is this variable
   delay(2000);
   servo2.write(cat);  
   servo3.write(cat);  
  }
  else if (digitalRead(button3)==HIGH){//paper
   Serial.println("button3");
   servo3.write(move_pull);  
   delay(100);   
   servo1.write(move_push);  
   delay(2000);
   servo3.write(cat);  
   servo1.write(cat);  
  }
  //}
  //else
   // Serial.print("no data");
  
}

