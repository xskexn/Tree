import java.util.*;
public class calculator {
    public static void main(String[] args){
    System.out.println("Welcome to the calculator");    
    Scanner input4 = new Scanner(System.in);
    Scanner input5 = new Scanner(System.in);
    Scanner input6 = new Scanner(System.in);
    System.out.print("Input a number: ");
    int num1 = input4.nextInt();
    System.out.println("Input an operator: ");
    String op = input5.next();
    System.out.print("Input a number: ");
    int num2 = input6.nextInt();
    if (op.equals("+")){
        System.out.println(num1 + num2);
    }else if (op.equals("-")){
        System.out.println(num1 - num2);
    }else if (op.equals("*")){
            System.out.println(num1 * num2);
        }else if (op.equals("/")){
            System.out.println(num1 / num2);
        }
    }
}
// TODO {}