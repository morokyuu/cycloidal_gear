include <param.scad>

difference(){
    union(){
        cylinder(h=l_eccebearing_h,r=d_eccebearing/2);
        cylinder(h=l_eccebearing_fr,r=d_eccebearing_fr/2);
    }
    cylinder(h=l_eccebearing_h,r=d_ecceshaft/2);
}
