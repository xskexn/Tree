package JvaLearningTree;

import java.util.Random;
import java.util.Scanner;

public class fccChallenge {
    public static void main(String[] args) {
        // Java Core Challenge 01
        int guessTrials = 5;
        Random random = new Random();
        System.out.println("Welcome!");
        System.out.print("Please input your name: ");
        Scanner scanner = new Scanner(System.in);
        String name = scanner.next();
        System.out.println("Hello " + name);
        System.out.println("Should we start the game? (Press 1 to start and any other number to end)");
        int choice = scanner.nextInt();
        if (choice == 1){
            System.out.println("Let's start the game...");
            System.out.println("Ok so... Rules of the game are simple! \n I generate a number between 0 and 20 and you have 5 tries to guess it! ok?");
            System.out.println("I'm now thinking of a number can you guess it? ");
            int randNum = random.nextInt(20) + 1;
            System.out.println(randNum);
            while (guessTrials > 0){
                System.out.print("Input your guess: ");
                int userChoice = scanner.nextInt();
                if (userChoice == randNum){
                    System.out.println("Good job " +  name + " You won! \nWith " + guessTrials  + " guesses left!");
                    System.out.println("The Game is OVER!");
                    System.out.println("Thank you " + name + " for playing!");
                }else{
                    guessTrials--;
                    System.out.println("Try Again!");
                    if (userChoice > randNum){
                        System.out.println("Your guess was higher than the number I'm thinking! \n you still have " + guessTrials + " left");
                    }else{
                        System.out.println("Your guess was lower than the number I'm thinking! \n you still have " + guessTrials + " left");
                    }
                }
            }
        } else {
            System.out.println("Next time then... ");
        }

    }
}
