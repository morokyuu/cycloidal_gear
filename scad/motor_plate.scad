include <base_plate.scad>

difference(){
    base_plate(36);
    
    translate([43/2,0,0])
    cylinder(h=10,r=3/2);
    translate([-43/2,0,0])
    cylinder(h=10,r=3/2);
}


