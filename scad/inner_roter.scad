include <param.scad>

//9-teeth
module roter(){
        linear_extrude(height=l_roter_thick,convexity=10)
        import(file="inner_roter.dxf");
}

//output-pin screw holes
module pinholes(){
    for(deg = [th_outp_angle : 360/4 : 360]){
        rotate([0,0,deg])
        translate([r_outp_position,0,0])
        cylinder(h=l_roter_thick,r=r_outp_schole);
    }
}

difference(){
    difference(){
        difference(){
            roter();
            pinholes();
        };
        //bearing hole
        cylinder(h=l_roter_thick,r=d_eccebearing/2);
    };
    //for bearing frange offset
    cylinder(h=l_eccebearing_fr,r=(d_eccebearing+4)/2);
}