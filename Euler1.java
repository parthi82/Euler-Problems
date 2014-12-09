
 /**
  * This program finds the sum of all multiple of 3 or 5
  * below 1000 and outputs them to standard output
  */

  public class Euler1 {

  	 public static void main(String[] args) {

      int sum = 0;

    
      for(int i = 0; i <= 1000; i++) {

         if( i % 3 == 0 || i % 5 == 0)
            sum += i;      

      }

      System.out.println(sum);

    }  

  }