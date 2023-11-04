include <param.scad>

difference(){
    cylinder(h=l_pole, r=d_pole/2);
    cylinder(h=l_pole, r=d_pole_hole/2);
}