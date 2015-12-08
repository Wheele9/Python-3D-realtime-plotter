//#include <avr/io.h>
/*const int sensorpin1=7;//sensor1
const int sensorpin2=6;//sensor2
const int sensorpin3=5;//sensor3
const int txpin=4;//Tx pin
unsigned long distance1,distance2,distance3;
unsigned long x,y,z;
unsigned long readsensor1();
unsigned long readsensor2();
unsigned long readsensor3();
void calccordinates(unsigned long,
unsigned long,unsigned long);*/

int x=0;int y=0; int z=0;

void setup()
{
Serial.begin(9600);

}
void loop()
{
//take sensor1 reading
x+=1;
y+=-1;
delay(175);


Serial.println("Sensor3 no reading");

calccordinates();
delay(500);
}//END OF MAIN LOOP FUNCTION

void calccordinates()
{

Serial.print(x);
Serial.print("\t");
Serial.print(y);
Serial.print("\t");
Serial.print(z);
Serial.print("\t");
Serial.println("");
}
