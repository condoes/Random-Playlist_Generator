#include <MFRC522.h>
#include <SPI.h>

#define RST_PIN   9    
#define SS_PIN    10 

MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup() {
  // put your setup code here, to run once:
   Serial.begin(9600);
   SPI.begin();
   mfrc522.PCD_Init();
}

void loop() {
  // put your main code here, to run repeatedly:
  if ( ! mfrc522.PICC_IsNewCardPresent()) {
    return;
  }
  
  if ( ! mfrc522.PICC_ReadCardSerial()) {
    return;
  }
 
  String content= "";
  byte letter;

  //reading & printing tag/card
  for (byte i = 0; i < mfrc522.uid.size; i++) {
     Serial.print(mfrc522.uid.uidByte[i] < 0x10);
     Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  delay(3000);
  Serial.println();
}
