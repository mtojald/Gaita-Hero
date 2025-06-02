#include <Wire.h>
#include <Adafruit_BMP085.h>

Adafruit_BMP085 bmp;

int ultimovalor = 0; // precisa ser fora do loop para manter o valor entre execuções

void setup() {
  Serial.begin(9600);
  if (!bmp.begin()) {
    Serial.println("Sensor BMP180 não encontrado. Verifique as conexões!");
    while (1); // trava o programa se o sensor não for encontrado
  }
}

void loop() {
  int valoratual = bmp.readPressure();
  
  Serial.print(valoratual);
  Serial.println(" Pa");

  if (valoratual > ultimovalor + 10) {  // diferença significativa
    Serial.println("Vermelho"); // O valor vermelho é substituido pela respectiva cor dependendo do sensor soprado. 
  }

  ultimovalor = valoratual;

}
