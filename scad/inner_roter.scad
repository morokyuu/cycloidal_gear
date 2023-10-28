$fa = 1;//5; //minimum=0.01
$fs = 0.1; //minimum=0.01

//9-teeth

ecce = 1.8;

difference(){
    linear_extrude(height=4,convexity=10)
    import(file="inner_roter.dxf");

    translate([ecce,0,0])
    cylinder(h=6,r=5);
};

