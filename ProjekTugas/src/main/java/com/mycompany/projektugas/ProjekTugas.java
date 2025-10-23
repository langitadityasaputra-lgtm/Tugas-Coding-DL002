/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.projektugas;

/**
 *
 * @author microsoft
 */
public class ProjekTugas {

    public static void main(String[] args) {
//     int a, b;
//
//    for (a=1; a<=1; a++) {
//        for (b=1; b<=1; b++) {
//            if (a<=b) {
//                System.out.print("     *");
//            }
//        }
//        System.out.println();
//    };
//
//    for (a=2; a<=2; a++) {
//        for (b=1; b<=5; b++) {
//            if (b<=a) {
//                System.out.print("   *");
//            }
//        }
//        System.out.println();
//    };
//    
//
//for (a=3; a<=3; a++) {
//        for (b=1; b<=5; b++) {
//            if (b<=a) {
//                System.out.print("  *");
//            }
//        }
//        System.out.println();
//    };
//
//    for (a=4; a<=4; a++) {
//        for (b=1; b<=5; b++) {
//            if (b<=a) {
//                System.out.print(" * ");
//            }
//        }
//        System.out.println();
//    };
    
    int a, b, c;

    for (a=1; a<=5; a++) {
        for (b=1; b<=5-a; b++) {
             System.out.print(" ");
        }
        for (c=1; c<=(2*a-1); c++){
            System.out.print("*");
        }
        System.out.println();
    };
        
        
        
    }
}
