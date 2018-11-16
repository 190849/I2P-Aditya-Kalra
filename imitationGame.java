import java.util.Scanner;

public class imitationGame
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Hello, welcome to my encrypter");
        System.out.println("Please input the code you would like to encrypt");
        String car = sc.nextLine();
        
        Encryption tester = new Encryption(car);
        System.out.println("This is your code encrypted: " + tester.encryptedCode());
        Decryption retester = new Decryption(tester.encryptedCode());
        System.out.println("Would you like your code to be decrypted?");
        
        String yesno = sc.nextLine();
        
        if(yesno.equals("yes"))
        {
            System.out.println("Your code decrypted is: " + retester.decryptedCode());
        }
        
        else
        {
            System.out.println("Hope you liked me encryption.");
        }
        
        
        
        
    }
    
    
    
    
}