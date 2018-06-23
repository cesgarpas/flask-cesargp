
#include <ArduinoJson.h>
#include "RestClient.h"


//Delay para dar un tiempo entre petición y petición
int requestDelay = 2000; 

//Credenciales Wifi
char* ssid = "SSID";
char* pass = "PASS";

//Url de la API REST
RestClient client = RestClient("flask-cesargp.herokuapp.com");
//RestClient client = RestClient("192.168.0.10",5000);

//Variable status
int status = 0;



///////////////////////////////////////// Setup /////////////////////////////////////////

void setup() {
  Serial.begin(115200);  
  Serial.println("Connecting to WiFi network ");
  client.begin(ssid, pass);
  Serial.println("Connected!");
  pinMode(LED_BUILTIN, OUTPUT);
}

///////////////////////////////////////// Loop /////////////////////////////////////////

void loop(){

  //Pecición del objecto JSON a almacenar en response
  Serial.println("Getting status info from URL...");
  String response;
  test_status(client.get("/led-status", &response));  //Se realiza la petición get

  //Parseado de el valor de status a un integer
  StaticJsonBuffer<300> JSONBuffer;
  JsonObject &parsed= JSONBuffer.parseObject(response);  
  status = parsed["ledStatus"];
  Serial.print("Integer value: ");
  Serial.println(status);

  //Encendido o apagado del LED
  if(status == 1)
  {
    Serial.println("Setting led On");
    digitalWrite(LED_BUILTIN, LOW);
  }
  else
  {
    Serial.println("Setting led Off");
    digitalWrite(LED_BUILTIN, HIGH);
  }

  //Delay para no spammear
  delay(requestDelay);
}

///////////////////////////////////////// Others /////////////////////////////////////////

//Función que indica si se ha completado o no con exito la petición
void test_status(int statusCode){
   delay(1000);
   if(statusCode == 200){
    Serial.print("TEST RESULT: ok (");
    Serial.print(statusCode);
    Serial.println(")");
   }else{
    Serial.print("TEST RESULT: fail (");
    Serial.print(statusCode);
    Serial.println(")");
   }
}



