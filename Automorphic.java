import java.util.Scanner;
import java.lang.Math;

public class AutomorphicNumber
{
    public static void main(String args[])
    {
        //Taking the number as input from the user using scanner class
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number :");
        int num = scan.nextInt();
        
        int squaredNum, temp, squaredNumRemainder, dig = 0;
        //Storing the number in a temporary variable to preserve original value
        temp = num;
        //Loop that counts the number of digits in a number
        while(temp>0)
        {
            temp = temp / 10;
            dig++;
        }

        //Finding the square of the number by using library function Math.pow()
        squaredNum = (int)Math.pow(num,2);
        squaredNumRemainder = squaredNum%(int)Math.pow(10, dig);
        if(squaredNumRemainder==num)
        {
            System.out.print(num+" is an Automorphic number");            
        }
        else
            System.out.print(num+" is not an Automorphic number");
    }
           }
