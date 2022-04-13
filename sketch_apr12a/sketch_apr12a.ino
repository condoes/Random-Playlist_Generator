#include <MFRC522.h>
#include <SPI.h>

#define RST_PIN   9    
#define SS_PIN    10 
#define KEY_RETURN 0xB0 //enter key

MFRC522 mfrc522(SS_PIN, RST_PIN);
char Enter = KEY_RETURN;

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
 
  //Serial.print("UID tag :");
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
  
//  Serial.println();
//  Serial.print("Message : ");
//  content.toUpperCase();
//  
//  if (content.substring(1) == "51 54 5F 26") {
//    Serial.println("Authorised access");
//    Serial.println();
//    delay(3000);
//  }
// 
// else {
//    Serial.println("Who are you?");
//    Serial.println();
//    delay(3000);
//  }
//
//}
