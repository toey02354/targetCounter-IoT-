#include <HCSR04.h>

float left, right;
float calculated_value;
int Threshold = 50;
int count1 = 0, count_RL = 0, count_LR = 0;

/* If the sensors do NOT work correctly, shuffle numbers of left and right
  left(11,10) and right(13,12)  left(13,12) and right(11,10) */
UltraSonicDistanceSensor distanceSensor_left(11, 10);
UltraSonicDistanceSensor distanceSensor_right(13, 12);
int out_l2r = 7; //right camera
int out_r2l = 8; //left camera

void setup() {
  pinMode(out_l2r, OUTPUT);
  pinMode(out_r2l, OUTPUT);
  Serial.begin(9600);
  Serial.println("Ready to work!");
}

void loop() {
  left = distanceSensor_left.measureDistanceCm();
  right = distanceSensor_right.measureDistanceCm();

  //key formula
  calculation();

  /* if the number from sensors (not from the key formula) is negative the result is noop (no operation),
    if the result is not negative it will go to the conditions loop */
  if ((left < 0) || (right < 0)) {
    //noop
  }
  else { //conditions
    if (abs(calculated_value) < Threshold) {
      digitalWrite(out_l2r, LOW);
      digitalWrite(out_r2l, LOW);
      //noop
    } else if (calculated_value < 0) {
      Serial.print("Animal is approaching! Be careful!\n");
      //      Serial.print("Left to Right\n");
      digitalWrite(out_l2r, HIGH);
      digitalWrite(out_r2l, LOW);
      count1 += 1;
      count_LR += 1;
      show_data();
    } else {
      Serial.print("Animal is Leaving!\n");
      //      Serial.print("Right to Left\n");
      digitalWrite(out_r2l, HIGH);
      digitalWrite(out_l2r, LOW);
      count1 += 1;
      count_RL += 1;
      show_data();
    }
  }
  right = 0;
  left = 0;
  calculated_value = 0;
}

void calculation() {
  //key formula
  calculated_value = left - right;
}

/* if you want to show something remove // from the black letters (do not remove from the grey letters) */
void show_data() {
  //print values of ultrasonic sensors
  //  Serial.print("Left: ");
  //  Serial.print(left);
  //  Serial.print("  Right: ");
  //  Serial.println(right);
  //print counter
  //  Serial.print("   Count_L2R : ");
  //  Serial.print(count_LR);
  //  Serial.print("   Count_R2L : ");
  //  Serial.print(count_RL);
  //  Serial.print("   Count(both directions) : ");
  //  Serial.println(count1);
  //print the result value
  //  Serial.print("Calculated_Value: ");
  //  Serial.println(calculated_value);
  delay(3000);
  //Serial.println("Ready for the nexy value\n");
}
