// Accelerometer Class - To be used for the Adafruit BNO055 Sensor interfacing with an Arduino.
// Author: Advait Ukidve (a.ukidve0220221@arts.ac.uk)
// License: This code is intended to be completely public domain and to be used under the Creative Commons CC0 License. No attribution is required, but any is welcome :)

/* Interfacing with an Arduino Leonardo over I2C:
BNO055 -----  Arduino
Vin    ---->  5V
GND    ---->  GND
SDA    ---->  SDA
SCL    ---->  SCL
*/


#include <Wire.h>                  // For communication with I2C device - the BNO055 sensor
#include <Adafruit_Sensor.h>       // Adafruit Unified Sensor Library - https://github.com/adafruit/Adafruit_Sensor 
#include <Adafruit_BNO055.h>       // Adafruit BNO055 Library - https://github.com/adafruit/Adafruit_BNO055 
#include <utility/imumaths.h>      // For vector calculations in BNO055 Library - https://github.com/adafruit/Adafruit_BNO055/blob/master/utility/imumaths.h 

// ACCELEROMETER CLASS DECLARATION ---------------------------------------------------------------------------------------------

class Accelerometer {             

// PRIVATE ----------------------------------------------------------------  
  private:

    int x;              // To store tilt along the x-axis (Roll)
    int y;              // To store tilt along the x-axis (Pitch)
    int z;              // To store tilt along the x-axis (Yaw)

    int latency;        // Latency of sending data - Check setUpAccelerometer() documentation below for more information on how to use.

    String output;      // String that save the output string in comma separated format i.e. "x,y,z" - Print this to console/serial monitor

    Adafruit_BNO055 bno = Adafruit_BNO055(55);   // BNO055 Object from Adafruit BNO055 Library
    sensors_event_t event;                       // Adafruit Unified Sensor Library Event struct to save event data

// PUBLIC ----------------------------------------------------------------  
  
  public:      

    // GETTERS -----------------------------------------------------------
    int getX() {         // Get x
      return x;
    }

    int getY() {         // Get y
      return y;
    }

    int getZ() {         // Get z
      return z;
    }

    int getLatency() {   // Get latency
      return latency;
    }

    // METHODS ------------------------------------------------------------------------

    // SETUP
    // Put in setup() of Arduino Programme. This sets up the Accelerometer object from the BNO055 Library and also adjusts the latency of the programme as an optional argument
    void setUpAccelerometer(int lat = 45) {   
      
      if(!bno.begin())            // Initialise the sensor
      {
        //Serial.print("No BNO055 was detected. Please check your connections");  // Test print statement
        while(1);
      }

      bno.setExtCrystalUse(true);  // Use external crystal for timing
      //delay(1000);

      latency = lat; // This adjusts the rate at which the programme sends data to the Serial Monitor
      /* 
      - Setting latency is a trade-off between the latency of the movement of the 
        player and camera in-game versus the impact of the natural shaking of one's hand.
      - For example, the minimum recommended latency of 30 will make the camera and player movements 
        smoother by sending data to the serial port every 30 milliseconds but will cause the game to 
        pick up the player's hand motions frequently resulting in camera jitter.
      - A latency close to the maximum recommended latency of 150 will send signals every 150 milliseconds
        making the camera less susceptible to hand jitter but will cause less smooth movement of the 
        player and camera.
      - The recommended range is between 30 and 150. The recommended value is 45.
      */
    }

    // MAP (NORMALISE) METHODS ------------------------------------------------------------------------------------------------------
    // Maps x, y, and z with default values
    void mapXYZ() {

      bno.getEvent(&event);        // Get event

      // Map respective raw sensor values to between -50 and 50 - Holding the sensor in 0,0,0 should yield output string 0,0,0
      // Change the values to change accuracy and range.
      x = map(event.orientation.x, 0, 360, -50, 50);        // Rotating the ball left to right
      y = map(event.orientation.y, -90, 90, -50, 50);       // Tilting the ball sideways
      z = map(event.orientation.z, -180, 180, -50, 50);     // Moving the ball front and back

    }


    // MODULAR MAP ------------------------------------------------------------------------------------------------------------------
    // Same as mapXYZ but 6 arguments set the min and max range for mapping x, y, and z respectively
    void modMapXYZ(float xMin = 0, float xMax = 360, float yMin = -90, float yMax = 90, float zMin = -180, float zMax = 180) {

      bno.getEvent(&event);        // Get event

      x = map(event.orientation.x, 0, 360, xMin, xMax);        // Rotating the ball left to right
      y = map(event.orientation.y, -90, 90, yMin, yMax);       // Tilting the ball sideways
      z = map(event.orientation.z, -180, 180, zMin, zMax);     // Moving the ball front and back

    }

    

    // RETURN STRING METHOD --------------------------------------------------------------------------------------------------------
    String createString() {       // (Ideally) put in loop() of Arduino Programme
      
      output = String(x) + "," + String(y) + "," + String(z);  // Create final string to send out over Serial
      return output;

    }
    

    // MODULAR CREATE STRING - CHOOSE WHETHER TO SEND X, Y, and Z VALUES INDIVIDUALLY-------------------------------------------------
    // Three arguments in booleans to choose whether to send x,y, and z values (in that order)
    String modCreateString(bool sendX, bool sendY, bool sendZ) {

      output.remove(0,output.length());  // Flush everything from output

      if (sendX) {
        output = String(x) + ",";
      }
      if(sendY) {
        output += String(y) + ",";
      }
      if(sendZ) {
        output += String(z);
      }

      return output;

    }

    // TEST STRING PRINT ---------------------------------------------------------------------------------------------------------------
    // For testing and calibration purposes - prints x,y,z with labels.
    // NOT RECOMMENDED to be sent to Serial Montor in final run as labels will require removal in the programme accessing the serial monitor.

    String testCreateString() {

      output = "X: " + String(x) + ", Y: " + String(y) + ", Z: " + String(z);  // Create final string to send out over Serial
      return output;

    }

    // END ------------------------------------------------------------------------------------------------------------------------------
    





















};