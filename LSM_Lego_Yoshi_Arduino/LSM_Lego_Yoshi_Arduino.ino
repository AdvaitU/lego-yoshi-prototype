#include "Accelerometer.h"   // Custom class created by Advait Ukidve. Find at https://github.com/AdvaitU/beginners-accelerometer-bno055
Accelerometer acc;           // Create object of the Accelerometer class// defines pins numbers

// Ultrasonic sensor setup
const int trigPin = 9;   // Trigger pin
const int echoPin = 10;  // Receive pin
long duration;            
int distance;

void setup() {
  
  Serial.begin(9600);

  acc.setUpAccelerometer(45);   // Accelerometer Setup function
  
  pinMode(2, INPUT);            // Buttons
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  
}

void loop() {

  acc.modMapXYZ(0, 720, 0, 720, 0, 720);   // Calibrates sensor readings to degrees
  if (acc.getX() <= 280) {                 // If figurine is rotated forward beyond 140 degrees
    Serial.println("5");
  }
  //Serial.println(acc.modCreateString(1,1,1));
  
  digitalWrite(trigPin, LOW);        // Ultrasonic sensor emit wave and receive wave
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH); // Reads the echoPin, returns the sound wave travel time in microseconds 
  distance = duration * 0.034 / 2;   // Calculates the distance

  // Pushbuttons
  if (distance <= 5) {
    Serial.println("4");
  }

  if (digitalRead(2) == HIGH) {
    Serial.println("1");
    //continue;
  }
  else if (digitalRead(3) == HIGH) {
    Serial.println("2");
  }
  else if (digitalRead(4) == HIGH) {
    Serial.println("3");
  }
  /*else if (digitalRead(5) == HIGH) {
    Serial.println("5");
  }*/
  else {}

  

  //delay(acc.getLatency());                             // Latency adjustment
  delay(500);
  
  }
