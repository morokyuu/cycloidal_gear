$fa = 1;//5; //minimum=0.01
$fs = 0.1; //minimum=0.01

//9-teeth

difference(){
    difference(){
        linear_extrude(height=4,convexity=10)
        import(file="inner_roter.dxf");

        cylinder(h=6,r=11);
    };
    
    for(deg = [22.5 : 360/4 : 360]){
        rotate([0,0,deg])
        translate([14,0,0])
        cylinder(h=6,r=2);
    }
};