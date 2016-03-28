int button1 = 2;
int button2 = 4;
int button3 = 6;
int paper = 0;
int plastic = 0;
int can = 0;

//this is the code i use to test the graph thingy
//combine this code with yours

void setup() {

  Serial.begin(9600);
 
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
}


void loop() {

  int paperButton = digitalRead(button1);
  int plasticButton = digitalRead(button2);
  int canButton = digitalRead(button3);
  
  if (paperButton == 1) {
    paper++; 
  }
  
  if (plasticButton == 1) {
    plastic++;
  }
  
  if (canButton == 1) {
    can++;
  }
  
  Serial.print(paper);
  Serial.print(" , ");
  Serial.print(plastic);
  Serial.print(" , ");
  Serial.println(can);
  delay(1000);
}
