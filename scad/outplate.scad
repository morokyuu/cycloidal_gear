include <param.scad>



GAP = 0.15;


difference(){
    //shaft
    cylinder(h=l_output_shaft_len,r=d_ecceshaft/2+tr_bearing_shaft);
    
    //d-cut
    translate([d_ecceshaft/2-0.5,-15,8])
    cube([10,30,20]);
}

translate([0,0,l_output_h])
cylinder(h=0.5,r=d_ecceshaft/2+0.8);

difference(){
    //plate
    cylinder(h=l_output_h, r=22);
    
    //output-holes
    for(deg = [0 : 360/4 : 360]){
        rotate([0,0,deg])
        translate([d_outp_position/2,0,0])
        cylinder(h=5,r=(d_output_hole)/2+GAP);
    }
}