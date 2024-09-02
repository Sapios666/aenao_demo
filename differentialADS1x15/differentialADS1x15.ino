#include <Adafruit_ADS1X15.h>

//#define TEST
//#define FUNC_PRINT
#define ALPHA 0.80

#define WINDOW 25 // How many samples will be stored in the median filter array
#define SAMPLING 50 // Sampling period in milliseconds

Adafruit_ADS1115 ads;  /* Use this for the 16-bit version */
// Adafruit_ADS1015 ads;     /* Use this for the 12-bit version */

float noLoadOffset = 92; // Prior to calibration the output voltage for zero load is 151mV.
float weightVoltageRatio = 4.12; // According to approximations the voltage drops 4.12mV for every kilogram added to the smart bin
float next, prev;
float filter[WINDOW];
int16_t results;
float voltage, weight;
/* Be sure to update this value based on the IC and the gain settings! */
float multiplier = 0.1875F; /* ADS1115  @ +/- 6.144V gain (16-bit results) */

void setup(void)
{
  Serial.begin(115200);
#ifdef TEST
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
  }

  for(int i=0; i<WINDOW; i++){
    filter[i] = 0;
  }

  results = ads.readADC_Differential_0_1();
  voltage = results * multiplier;
  weight = (voltage - noLoadOffset) / weightVoltageRatio;
  prev = weight;
}

void loop(void)
{
  float median;

#ifdef TEST
  results = ads.readADC_Differential_0_1();
  voltage = results * multiplier;
  // Serial.print("Differential: "); Serial.print(results); Serial.print("("); Serial.print(results * multiplier); Serial.println("mV)");
  // Serial.print(voltage); Serial.print("mV\t");
  // Serial.print(weight); Serial.print("kg\n");
  Serial.println(voltage);
  delay(SAMPLING);
#else
  for(int i=0; i<WINDOW; i++) {
    results = ads.readADC_Differential_0_1();
    voltage = results * multiplier;
    weight = (voltage - noLoadOffset) / weightVoltageRatio;
    next = weight*(1-ALPHA) + prev*ALPHA;
    prev = next;
    filter[i] = next;
    // Serial.println(filter[i]);
    delay(SAMPLING);
  }
  
  median = median_filter(filter);
  Serial.println(median);
#endif
}

void fifo(float value)
{
  for(int i=1; i<WINDOW; i++) {
    filter[i-1] = filter[i];
  }
  filter[WINDOW-1] = value;

  for(int i=0; i<WINDOW; i++) {
    Serial.print(filter[i]);
    Serial.print(" ");
  }
  Serial.print("\n");
}

float median_filter(float * array)
{
  float temp;

#ifdef FUNC_PRINT
  for(int i=0; i<WINDOW; i++) {
    Serial.print(array[i]);
    Serial.print(" ");
  }
#endif

  for(int i=0; i<WINDOW; i++) {
    for(int j=i+1; j<WINDOW; j++) {
      if(array[i]>array[j]) {
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
      }
    }
  }

#ifdef FUNC_PRINT
  Serial.print("\n");
  for(int i=0; i<WINDOW; i++) {
    Serial.print(array[i]);
    Serial.print(" ");
  }
  Serial.print("\n");
#endif

  return array[(int)WINDOW/2];
}
