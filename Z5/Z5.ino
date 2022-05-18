#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 9
#define SS_PIN 10

byte readCard[4];
String MasterTag = "A9A785B9";  
String tagID = "";

MFRC522 mfrc522(SS_PIN, RST_PIN);

void setup() 
{
  SPI.begin(); 
  mfrc522.PCD_Init(); 
  Serial.begin(9600);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(8, OUTPUT);

  Serial.print(" Access Control\n");
  Serial.print("Scan Your Card>>\n");
}

void loop() 
{
  
  while (getID()) 
  {  

    digitalWrite (8, HIGH);
    delay (400);
    digitalWrite (8, LOW);
    
    if (tagID == MasterTag) 
    {
      digitalWrite(6, HIGH);
      Serial.print(" Access granted!\n");
      
    }
    else
    {
      digitalWrite(5, HIGH);
      Serial.print(" Access Denied!\n");
    }

    Serial.print(" ID : ");
    Serial.print(tagID);
    Serial.print("\n");
      
    delay(2000);

    digitalWrite(5, LOW);
    digitalWrite(6, LOW);
    Serial.print(" Access Control\n");
    Serial.print("Scan Your Card>>\n");
  }
}


boolean getID() 
{

  if ( ! mfrc522.PICC_IsNewCardPresent()) {
  return false;
  }
  if ( ! mfrc522.PICC_ReadCardSerial()) {
  return false;
  }
  tagID = "";
  for ( uint8_t i = 0; i < 4; i++) { 
  tagID.concat(String(mfrc522.uid.uidByte[i], HEX)); 
  }
  tagID.toUpperCase();
  mfrc522.PICC_HaltA(); 
  return true;
}
