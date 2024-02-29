public class CalcLCM 
{
  public static void main(String[] args) 
{

    int num1 = 15, num2 = 21, lcm;

    // biggest number between the two stored in lcm
    lcm = (num1 > num2) ? num1 : num2;

    // to minimize the loop iterations we start by checking both the numbers from biggest number i.e. lcm
    while(true)
    {
    // keep on checking lcm with num1 and num2 
    // until both num1 and num2 are perfectly divisible with lcm
      if( lcm % num1 == 0 && lcm % num2 == 0 ) 
      {
        System.out.printf("The LCM is %d",lcm);
        break;
      }
      ++lcm;
    }
  }
} 
