int pin1 = A0;
int val = 0;

void setup () {
Serial.begin(9600);
}

void loop () {
val = analogRead(pin1);


  Serial.println(val);
delay(5);
}
