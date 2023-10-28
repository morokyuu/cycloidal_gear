$fa = 5; //minimum=0.01
$fs = 0.1; //minimum=0.01

ecce = 1.8;
din = 10;

difference(){
    union(){
        cylinder(h=1,r=din/2+1);
        cylinder(h=13,r=din/2,center=false);
    }
    translate([ecce,0,0])
    cylinder(h=13,r=5/2);
};

