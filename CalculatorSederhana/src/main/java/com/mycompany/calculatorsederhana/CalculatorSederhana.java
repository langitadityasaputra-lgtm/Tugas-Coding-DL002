/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.calculatorsederhana;

import java.util.Scanner;

/**
 *
 * @author microsoft
 */
public class CalculatorSederhana {

    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        int tombol;
        char balen;
        do{
        System.out.println("====== <Calculator Sederhana wahaha> ======");
        System.out.println("|   1. penjumlahan     |");
        System.out.println("|   2. pengurangan     |");
        System.out.println("|   3. perkalian       |");
        System.out.println("|   4. pembagian       |");
        System.out.println("|   5. pencarian sisa  |");
        System.out.println("|   6. pencarian akar  |");
        System.out.println("|   7. pangkat         |");
        
        System.out.println("pilih salah satu metode perhitungan diatas dari 1-7");
        
        System.out.println("===========================================");

        tombol = input.nextInt();
        
        switch(tombol){
            case 1:
                int a,b;
               System.out.println("|   jumlahkan nomor   |");
                System.out.print("|   ");
                a = input.nextInt();
               System.out.println("|   dengan nomor      |");
                System.out.print("|   ");
                b = input.nextInt();
                            System.out.print("|   maka hasile: ");
                                System.out.println(a+b);
            
            break;
            
            case 2:
               System.out.println("|   kurangi nomor   |"); 
                System.out.print("|   ");
                a = input.nextInt();
                        System.out.println("|   dengan nomor   |");
                System.out.print("|   ");
                b = input.nextInt();
                            System.out.print("|   maka hasile: ");
                                System.out.println(a-b);
               
            break;
            
            case 3:
               System.out.println("|   Kalikan nomor   |");
                System.out.print("|   ");
                a = input.nextInt();
                        System.out.println("|   dengan nomor   |");
                System.out.print("|   ");
                b = input.nextInt();
                            System.out.print("|   maka hasile: ");
                                System.out.println(a*b);
                                
            break;
            
            case 4:
               System.out.println("|   bagikan nomor   |");
                System.out.print("|   ");
                a = input.nextInt();
                        System.out.println("|   dengan nomor   |");
                System.out.print("|   ");
                b = input.nextInt();
                            System.out.print("|   maka hasile: ");
                                System.out.println(a/b);
                                
            break;
            
            case 5:
               System.out.println("|   masukno nomor   |");
                System.out.print("|   ");
                a = input.nextInt();
                        System.out.println("|   bagi nomor   |");
                System.out.print("|   ");
                b = input.nextInt();
                            System.out.print("|   maka hasile: ");
                                System.out.println(a%b);
            break;
            
            case 6:
               System.out.println("|   masukno nomor   |");
                System.out.print("|   ");
                a = input.nextInt();
                        System.out.println("|   akar nomor   |");
                            System.out.print("|   maka hasile: ");
                                System.out.println(Math.sqrt(a));
            break;
            case 7:
               System.out.println("|   masukno nomor   ");
                System.out.print("|   ");
                a = input.nextInt();
                    System.out.println("|   akarno ambek nomor   |");
                    System.out.print("|   ");
                b = input.nextInt();
                        System.out.print("|   maka hasile   |");
                                System.out.println(Math.pow(a, b));
            break;
          
            default : System.out.println("pilihanmu gaonok cuy, deloken pilihane opo ikulo");
            
            break;}
             System.out.println("pengen baleni to mandek?");
             System.out.println("ketik -y- gawe baleni to -moh- mandek");
             balen = input.next().charAt(0);
       }
        while(balen == 'y' || balen == 'Y');
        System.out.println("maturnuwun wis gawe calculator, program mandek");
        input.close();
        
        System.out.println("===========================================");
    }
}
