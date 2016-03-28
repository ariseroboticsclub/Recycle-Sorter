

// include the library code:
#include <LiquidCrystal.h>

  String items[3] = {"Plastic:"," Tims:", " Cans:"};
  int counter[3] = {0,0,0};
  int stringLenght = items[0].length() + items[1].length() + items[2].length() + 3;
  
  

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(8, 9, 10, 11, 12, 13);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  
  
}

void loop() {
  
  lcd.clear();
  displayer();
  for (int positionCounter = 0; positionCounter < 25; positionCounter++) {
    // scroll one position left:
    lcd.scrollDisplayLeft();
    // wait a bit:
    delay(150);
  }
  lcd.clear();
  lcd.setCursor(15,0);
  displayer();
    for (int positionCounter = 15; positionCounter > 0; positionCounter--) {
    // scroll one position left:
    lcd.scrollDisplayLeft();
    // wait a bit:
    delay(150);
  }
  
}

void displayer(){
  lcd.print(items[0] + String(counter[0]));
  lcd.print(items[1] + String(counter[1]));
  lcd.print(items[2] + String(counter[2]));
}

void increment(int item){
    counter[item]++;
  }




