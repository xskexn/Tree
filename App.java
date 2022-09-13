import java.util.*;
public class App{
    public static void main(String[] args){
        // TODO Login page
        // TODO Calculator
        // TODO Class
        // If you wonder why i do login page so often is beacause im out of idea 
        // and i just know the bare basic of this launguage.
              
        System.out.println("Hi Welcome to LCW login page");
        System.out.print("Input Username... ");
            Scanner input0 = new Scanner(System.in);
        String username = input0.nextLine();
        System.out.print("Input Password... ");
            Scanner input1 = new Scanner(System.in);
        String password = input1.nextLine();
        System.out.println("Well Done.... " + "\n" + "Now verify and you are all done!");
            Scanner input2 = new Scanner(System.in);
        System.out.println("Input Username... ");
            Scanner input3 = new Scanner(System.in);
        String newUsername = input2.nextLine();
        System.out.print("Input Password... ");
        String newPassword = input3.nextLine();
        while (!newUsername.equals(username)){
            if (newUsername.equals(username)){
                System.out.println(username + " Acces approved!");
            } else {
                System.out.println("Input Username... ");
                newUsername = input2.nextLine();
                System.out.println("Acces on username Denied!");
            }
        }
        while (!password.equals(newPassword)){
            if (newPassword.equals(password)){
                System.out.println("Acces Approved!");
            } else {
                newPassword = input3.nextLine();
                System.out.print("Input Password... ");
                System.out.println("Acces on password Denied!");
            }
            // TODO Calculator
            }
        }
    }
//{}