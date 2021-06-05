// This #include statement was automatically added by the Particle IDE.
#include <HttpClient.h>

// This #include statement was automatically added by the Particle IDE.
#include <Grove_LCD_RGB_Backlight.h>

HttpClient http;

rgb_lcd lcd;

const int colorR = 255;
const int colorG = 0;
const int colorB = 255;

const int SoundSensor = A0;
const int LightSensor = A1;
const int buttonPin = 2;


int buttonState = 0;

int lightOnTimer;
int lightOffTimer;

bool isLightOn = false;

http_header_t headers[] = {
    {"Accept", "*/*"},
    {NULL, NULL}
};

http_request_t request;
http_response_t response;

const int LightThreshold = 800;
const int SoundThreshold = 700;
const int httpDelay = 10000;

unsigned int nextTime = 0;

void setup() {
    Serial.begin(9600);
    
    pinMode(buttonPin, INPUT);
    
    lcd.begin(16,2);
    
    lcd.setRGB(colorR, colorG, colorB);
    
    lcd.print("CS147 PROJECT");
    lcd.setCursor(0, 1);
    lcd.print("Calibrating...");
    
    lightOffTimer = millis();

}

void loop() {
    buttonState = digitalRead(buttonPin);
    
    if (buttonState){
        if (isLightOn){
            lightOff();
        }
        else{
            lightOn();
        }
        
    }
    
    
    int soundValue = analogRead(SoundSensor);
    int lightValue = analogRead(LightSensor);
    // Serial.print(soundValue);
    // Serial.print("\t");
    // Serial.println(lightValue);
    // Serial.print("Button State: ");
    // Serial.println(buttonState);
    
    if (lightValue < LightThreshold){

        if (soundValue > SoundThreshold){
            lightOn();
            
        }
        else if(millis() > lightOnTimer){
            lightOff();
            
        }
    }
    else if(millis() > lightOnTimer) {
        lightOff();
    }
    
    if (millis() > nextTime){
        request.hostname = "192.168.86.37";
        request.port = 5000;
        request.path = "/?lightStatus=" + String(isLightOn) + "&lightValue=" + String(lightValue)  + "&soundValue=" + String(soundValue);
        
        http.get(request, response, headers);
        Serial.print("Application>\tResponse status: ");
        Serial.println(response.status);
            
        // Serial.print("Application\t HTTP Response Body: ");
        // Serial.println(response.body);
        
        nextTime = millis() + httpDelay;
    }

    delay(200);
  

}

void lightOn(){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Light: ON");
    lightOnTimer = millis() + 10000;
    isLightOn = true;
}

void lightOff(){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Light: OFF");
    isLightOn = false;
}