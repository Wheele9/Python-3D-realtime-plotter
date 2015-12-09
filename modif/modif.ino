#include <avr/io.h>
const int sensorpin1=7;//sensor1
const int sensorpin2=6;//sensor2
const int sensorpin3=5;//sensor3
const int txpin=4;//Tx pin
unsigned long distance1,distance2,distance3;
unsigned long x,y,z;
unsigned long readsensor1();
unsigned long readsensor2();
unsigned long readsensor3();
void calccordinates(unsigned long,
unsigned long,unsigned long);
void setup()
{
Serial.begin(9600);
DDRD |= B11110000;
PORTD &= B00001111;
}
void loop()
{
//take sensor1 reading
distance1=readsensor1();
delay(75);
distance2=readsensor2();
delay(75);
distance3=readsensor3();
delay(75);
if(distance1==0){
Serial.println("Sensor1 no reading");
}

if(distance2==0){
Serial.println("Sensor2 no reading");
}

if(distance3==0){
Serial.print("Sensor3 no reading");
}

calccordinates(distance1,distance2,distance2);
delay(500);
}//END OF MAIN LOOP FUNCTION
unsigned long readsensor1()
{
pinMode(sensorpin1,OUTPUT);
pinMode(txpin,OUTPUT);
digitalWrite(sensorpin1,HIGH);
digitalWrite(txpin,HIGH);
delayMicroseconds(5);
digitalWrite(sensorpin1,LOW);
digitalWrite(txpin,LOW);
pinMode(sensorpin1,INPUT);
distance1=pulseIn(sensorpin1,HIGH);
distance1=distance1/29;
return distance1;
}
unsigned long readsensor2()
{
pinMode(sensorpin2,OUTPUT);
pinMode(txpin,OUTPUT);
digitalWrite(sensorpin2,HIGH);
digitalWrite(txpin,HIGH);
delayMicroseconds(5);
digitalWrite(sensorpin2,LOW);
digitalWrite(txpin,LOW);
pinMode(sensorpin2,INPUT);
distance2=pulseIn(sensorpin2,HIGH);
distance2=distance2/29;
return distance2;
}
unsigned long readsensor3()
{
pinMode(sensorpin3,OUTPUT);
pinMode(txpin,OUTPUT);
digitalWrite(sensorpin3,HIGH);
digitalWrite(txpin,HIGH);
delayMicroseconds(5);
digitalWrite(sensorpin3,LOW);
digitalWrite(txpin,LOW);
pinMode(sensorpin3,INPUT);
distance3=pulseIn(sensorpin3,HIGH);
distance3=distance3/29;
return distance3;
}
void calccordinates(unsigned long d1,
unsigned long d2,unsigned long d3)
{
z=((d1*d1)-(d3*d3)+2.25)/3;
y=((d1*d1)-(d2*d2)+2.25)/3;
x=sqrt((d1*d1)-(y*y)-(z*z));
if(x<0){
x=-x;
}

Serial.print(x);
Serial.print("\t");
Serial.print(y);
Serial.print("\t");
Serial.print(z);
Serial.print("\t");
Serial.println("");
}
