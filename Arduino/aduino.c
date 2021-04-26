#include <Servo.h>

 

Servo myservo1;

String bar_data = "";

Servo myservo2;

Servo myservo5;

Servo myservo6;

 

void setup()

{

  Serial.begin(9600);

//  Serial.available();

  myservo1.attach(12); //12=hadong

  myservo1.write(0);

  myservo2.attach(7);  //7=jidong

  myservo2.write(0);

  myservo5.attach(8);  //8=yeonmudong

  myservo5.write(180);

  myservo6.attach(13);  //9=iuidong

  myservo6.write(180);

}

 

 

void loop()

{

  

  //char bar_data = Serial.read();

  while (Serial.available()>0)

  {

    bar_data += (char)Serial.read();

  }

  

  //Serial.println(bar_ data);

  

  if (bar_data == "hadong")

  {

    delay(11000);

    Serial.println(bar_data);    // Test

    Serial.println("Im changed!"); // Test

    myservo1.write(50); //hadong board

    //myservo2.write(0); //test board

    bar_data = "";

    delay(5000);

    myservo1.write(0);

  }

  

  else if (bar_data == "jidong")

  {

    delay(13000);

    Serial.println(bar_data);    // Test

    Serial.println("Im changed!"); // Test

    myservo2.write(55); //hadong board

    //myservo2.write(0); //test board

    bar_data = "";

    delay(5000);

    myservo2.write(0);    

  }

  else if (bar_data == "yeonmudong")

  {

    delay(13500);

    Serial.println(bar_data);    // Test

    Serial.println("Im changed!"); // Test

    myservo5.write(120); //hadong board

    //myservo2.write(0); //test board

    bar_data = "";

    delay(5000);

    myservo5.write(180);    

    

  }

  else if (bar_data == "iuidong")

  {

    delay(10000);

    Serial.println(bar_data);    // Test

    Serial.println("Im changed!"); // Test

    myservo6.write(120); //hadong board

    //myservo2.write(0); //test board

    bar_data = "";

    delay(5000);

    myservo6.write(180);    

  }

  

  delay(100);

}