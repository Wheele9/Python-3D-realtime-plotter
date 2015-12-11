
const int sensorpin1=7;//sensor1
const int sensorpin2=6;//sensor2
const int sensorpin3=5;//sensor3
const int txpin=4;//Tx pin
unsigned long distance1,distance2,distance3;
unsigned long x=0;unsigned long y=2;unsigned long z=3;
unsigned long readsensor1();
unsigned long readsensor2();
unsigned long readsensor3();
void calccordinates(unsigned long,
unsigned long,unsigned long);
void setup()
{
Serial.begin(9600);

}
void loop()
{
//take sensor1 reading

delay(75);

delay(75);

delay(75);

x=x+1;
y=y+2;
z=z;


calccordinates(distance1,distance2,distance2);
delay(500);
}//END OF MAIN LOOP FUNCTION

void calccordinates(unsigned long d1,
unsigned long d2,unsigned long d3)
{


Serial.print(x);
Serial.print("\t");
Serial.print(y);
Serial.print("\t");
Serial.print(z);
Serial.print("\t");
Serial.println("");
}
