int button1 = 2;
int button2 = 4;
int paper = 0;
int plastic = 0;

//this is the code i use to test the graph thingy
//combine this code with yours

void setup() {

  Serial.begin(9600);
 
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
}


void loop() {

  int paperButton = digitalRead(button1);
  int plasticButton = digitalRead(button2);
  
  if (paperButton == 1) {
    paper++;
   
  }
  
  if (plasticButton == 1) {
    plastic++;
 
  }
  
  Serial.print(paper);
  Serial.print(" , ");
  Serial.println(plastic);
  delay(1000);
}
