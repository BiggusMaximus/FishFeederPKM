#include <Arduino.h>

int PH_4502c = A1; 
int SAMPLE = 100;
double PH;
double SLOPE_PH  = -0.0426;
double INTERCEPT_PH = 38.093;


void pHInitialization() {
  pinMode(PH_4502c, INPUT);
}

double PH_Akhir (){
  for (int i = 0; i <= SAMPLE; i++){
    PH +=analogRead (PH_4502c);
  }
  PH /= SAMPLE;
  return PH;
}

double measure_pH() {
  // Read the analog value from pH sensor
  double PH_last = SLOPE_PH*PH_Akhir() + INTERCEPT_PH;
  return PH_last;
}

