#include <Servo.h>
#include <LiquidCrystal.h>

Servo servo1, servo2, servo3; // Define servos
LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

String items[3] = {"Plastic:"," Tims:", " Cans:"};
int counter[3] = {0,0,0};

 
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
  lcd.begin(16,2);
  
  servo1.attach(3); 
  servo2.attach(2);
  servo3.attach(4);
  servo1.write(cat);
  servo2.write(cat);
  servo3.write(cat);
  Serial.begin(9600);
  displayer();
  pinMode(button1,INPUT);
  pinMode(button2,INPUT);
  pinMode(button3,INPUT);
}
void loop() {
  
  if (digitalRead(button1)==HIGH){//plastic
  Serial.println("button1");
   servo2.write(move_push);  //pushed
   delay(100);   
   servo1.write(move_pull);  //pulled back
   increment(0);
   lcd.clear();
   displayer();
   delay(2000);
   servo2.write(cat);  
   servo1.write(cat);
  
  }


  else if (digitalRead(button2)==HIGH){//aluminium
  Serial.println("button2");
   servo2.write(move_pull);  //push in this case is this variable
   delay(100);   
   servo3.write(move_push);  //pull in this case is this variable
   increment(1);
   lcd.clear();
   displayer();
   delay(2000);
   servo2.write(cat);  
   servo3.write(cat); 
 
  }
  else if (digitalRead(button3)==HIGH){//paper
   Serial.println("button3");
   servo3.write(move_pull);  
   delay(100);   
   servo1.write(move_push);  
   increment(2);
   lcd.clear();
   displayer();
   delay(2000);
   servo3.write(cat);  
   servo1.write(cat);  

  }

  
}
void increment(int item){
    counter[item]++;
  }

void displayer(){
  lcd.print(items[0] + String(counter[0]));
  lcd.print(items[1] + String(counter[1]));
  lcd.setCursor(0,2);
  lcd.print(items[2] + String(counter[2]));
  lcd.setCursor(9,2);
  lcd.print("ARISE");
}


void sweep(){
  for (int positionCounter = 0; positionCounter < 25; positionCounter++) {
    // scroll one position left:
    lcd.scrollDisplayLeft();
    // wait a bit:    
  }

}

