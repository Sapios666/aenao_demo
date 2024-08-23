#include <Adafruit_ADS1X15.h>

// #define MESSAGES

Adafruit_ADS1115 ads;  /* Use this for the 16-bit version */
// Adafruit_ADS1015 ads;     /* Use this for the 12-bit version */

float noLoadOffset = 0.151; // Prior to calibration the output voltage for zero load is 151mV.
float weightVoltageRatio = 0.00412; // According to approximations the voltage drops 4.12mV for every kilogram added to the smart bin

void setup(void)
{
  Serial.begin(115200);
#ifdef MESSAGES
  Serial.println("Hello!");
  Serial.println("Getting differential reading from AIN0 (P) and AIN1 (N)");
#endif

  // The ADC input range (or gain) can be changed via the following
  // functions, but be careful never to exceed VDD +0.3V max, or to
  // exceed the upper and lower limits if you adjust the input range!
  // Setting these values incorrectly may destroy your ADC!
  //                                                                ADS1015  ADS1115
  //                                                                -------  -------
  ads.setGain(GAIN_TWOTHIRDS);  // 2/3x gain +/- 6.144V  1 bit = 3mV      0.1875mV (default)
  // ads.setGain(GAIN_ONE);        // 1x gain   +/- 4.096V  1 bit = 2mV      0.125mV
  // ads.setGain(GAIN_TWO);        // 2x gain   +/- 2.048V  1 bit = 1mV      0.0625mV
  // ads.setGain(GAIN_FOUR);       // 4x gain   +/- 1.024V  1 bit = 0.5mV    0.03125mV
  // ads.setGain(GAIN_EIGHT);      // 8x gain   +/- 0.512V  1 bit = 0.25mV   0.015625mV
  // ads.setGain(GAIN_SIXTEEN);    // 16x gain  +/- 0.256V  1 bit = 0.125mV  0.0078125mV

  if (!ads.begin()) {
    Serial.println("Failed to initialize ADS.");
    while (1);
  }}

void loop(void)
{
  int16_t results;
  float voltage, weight;

  /* Be sure to update this value based on the IC and the gain settings! */
  // float   multiplier = 3.0F;    /* ADS1015 @ +/- 6.144V gain (12-bit results) */
  float multiplier = 0.1875F; /* ADS1115  @ +/- 6.144V gain (16-bit results) */

  results = ads.readADC_Differential_0_1();
  voltage = results * multiplier;
  weight = (voltage - noLoadOffset) / weightVoltageRatio;

#ifdef MESSAGES
  // Serial.print("Differential: "); Serial.print(results); Serial.print("("); Serial.print(results * multiplier); Serial.println("mV)");
  Serial.print(voltage); Serial.print("V\t");
  Serial.print(weight); Serial.print("kg\n");
  delay(1000);
#else
  Serial.println(weight);
  delay(100);
#endif
}
