include <param.scad>

//9-teeth
module roter(){
        linear_extrude(height=l_roter_thick,convexity=10)
        import(file="inner_roter.dxf");
}

//output-pin
module output_pins(){
    for(deg = [th_outp_angle : 360/4 : 360]){
        rotate([0,0,deg])
        translate([d_outp_position/2,0,0])
        cylinder(h=l_roter_thick+5,r=d_outp_diameter/2);
    }
}

difference(){
    union(){
        roter();
        output_pins();
    };
    //bearing hole
    cylinder(h=l_roter_thick,r=d_eccebearing/2);
};
