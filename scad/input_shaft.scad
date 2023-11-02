$fa = 5; //minimum=0.01
$fs = 0.1; //minimum=0.01

ecce = 1.8;
d_ecceshaft = 8;
d_eccebearing = 14;

d_motshaft = 5;
l_motshaft = 8;//13;

d_shaftholder = 10;

module shaft_hole(){
    hull(){
        translate([0,0,l_motshaft+6])
        cylinder(h=0.1,r=0.1);
        cylinder(h=l_motshaft,r=d_motshaft/2);
    }
}

module shaft_holder(){
    union(){
        //shaft holder
        cylinder(h=l_motshaft+10,r=d_shaftholder/2,center=false);
        //eccentric shaft
        translate([ecce,0,0])
        cylinder(h=l_motshaft+15,r=d_motshaft/2);
    }
}

difference(){
    shaft_holder();
    shaft_hole();
}
