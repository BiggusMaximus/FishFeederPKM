#include <Arduino.h>

int TDS_SENSOR = A7;
double SLOPE_TDS = 7.206;
double INTERSECT_TDS = -121.53;

void TDSInitialization() {
  pinMode(TDS_SENSOR, INPUT);
}

double TDS_S (){
  double TDS = 0;
  for (int i = 0; i<=SAMPLE; i++){
    TDS += double(analogRead (TDS_SENSOR));
  }
  TDS /= SAMPLE;
  return TDS;
}

double measure_TDS() {
  // put your main code here, to run repeatedly:
  double TDS_AKHIR = SLOPE_TDS*TDS_S() + INTERSECT_TDS;
  return TDS_AKHIR;

}

