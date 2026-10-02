#include <Arduino.h>
#include <IRremote.h>
#include "command_codes.h"

#define SERIAL_PORT 9600
#define TR_PIN 3
#define REP_ARROW 3

int commandToCode(String command) {
  if (command == STR_LEFT) return HEX_LEFT;
  if (command == STR_RIGHT) return HEX_RIGHT;
  if (command == STR_A) return HEX_A;
  if (command == STR_B) return HEX_B;
  if (command == STR_C) return HEX_C;
  if (command == STR_D) return HEX_D;
  if (command == STR_E) return HEX_E;
  if (command == STR_F) return HEX_F;
  if (command == STR_G) return HEX_G;
  if (command == STR_H) return HEX_H;
  if (command == STR_I) return HEX_I;
  if (command == STR_J) return HEX_J;
  if (command == STR_U) return HEX_U;
  if (command == STR_L) return HEX_L;
  if (command == STR_INITIAL) return HEX_INITIAL;
  if (command == STR_MEMORY) return HEX_MEMORY;
  else return NULL_HEX;
}

void setup() {
  Serial.begin(SERIAL_PORT);
  IrSender.begin(TR_PIN);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    int code = commandToCode(command);

    int repeats = 0;
    repeats = (code == HEX_LEFT || code == HEX_RIGHT) ? REP_ARROW : 1;

    // Talvez mudar as mensagens...
    if (code != 0x0) {
      Serial.print("SENT");
      IrSender.sendNEC(0x0, code, repeats);
    } else {
      Serial.println("ERROR");
    }
  }
}
