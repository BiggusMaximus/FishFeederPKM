#include <Arduino.h>
#include "pH.h"
#include "TDS.h"

void setup() {
  Serial.begin(9600);
  pHInitialization();
  TDSInitialization();
}

void loop() {
  double pH = measure_pH();
  double TDS = measure_TDS();
  Serial.println(String(pH) + "," + String(TDS));
}
