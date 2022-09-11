//connect your joystick JRX to pin A5
//and JRY to A4

void setup() {
  Serial.begin(9600);
}
void loop() {
  int x = analogRead(A4);
  int y = analogRead(A5);
  Serial.print('x');
  Serial.println(x);
  Serial.print('y');
  Serial.println(y);
}
