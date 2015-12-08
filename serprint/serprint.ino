/*
Uses a FOR loop for data and prints a number in various formats.
*/
int x = 0;    // variable

void setup() {
  Serial.begin(9600);      // open the serial port at 9600 bps:    
}

void loop() {  


  for(x=0; x< 64; x++)
  {    // only part of the ASCII chart, change to suit

    // print it out in many formats:
    Serial.print(x);       // print as an ASCII-encoded decimal - same as "DEC"
    Serial.print("\t");    // prints a tab

    Serial.print(2*x);       // print as an ASCII-encoded decimal - same as "DEC"
    Serial.print("\t");    // prints a tab


    Serial.print(3*x);       // print as an ASCII-encoded decimal - same as "DEC"
    Serial.print("\t");    // prints a tab

               // delay 200 milliseconds
    Serial.println("");
    delay(0.1); 
  }
   // prints another carriage return
}
