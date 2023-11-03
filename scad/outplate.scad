include <param.scad>



difference(){
    cylinder(h=3, r=22);
    
    for(deg = [0 : 360/4 : 360]){
        rotate([0,0,deg])
        translate([d_outp_position/2,0,0])
        cylinder(h=5,r=d_output_hole/2);
    }
}