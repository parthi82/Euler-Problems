
  /**
   * This program prints the sum of all even number
   * in fibonacci series below 4 million (4000000)
   */

   public class Euler2 {

   	  public static void main(String[] args) {

   	  	  int fibA = 0;
   	  	  int fibB = 1;
   	  	  int fibC = 0;
          int total = 0;

          while(true) {

          	  fibC = fibA + fibB; // sum previous two terms to get next term
          	  fibA = fibB; // advance to next term
          	  fibB = fibC;

          	  if(fibC > 4000000) 
          	  	break;

          	  if(fibC % 2 == 0) 
          	  	total += fibC;

          }

          System.out.println(" Sum of all even numbers not exceeding 4 million in fibonacci series is " + total);
   	  }
   }