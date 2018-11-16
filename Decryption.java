
public class Decryption
{
    
    String code;
    
    public Decryption(String theCode) //my constructor for the code. Intialising my varibale
    {
        code = theCode;
    }
    
    public String decryptedCode()
    {
    String reversefinalCode = "";
    int[] characterArray = new int[code.length()]; //defining my array which will be the length of the string of the code 
    
    for (int i = 0; i < code.length(); i++){ //in this for loop my code will  
        int num = (int)(code.charAt(i));
        num = num - 1;
        characterArray[i] = num;

    }
    
    for(int i = 0; i < characterArray.length; i++)//for each loop that runs the loop for every element in the array. every element is equal to i 
    {
        char theChar = (char) characterArray[i];
        String theLetter = Character.toString(theChar); //to string converts the character to a string 
        reversefinalCode += theLetter; //this concatinates the individual character length strings into one big string 
    
    
    
}
return reversefinalCode;
}
}
    
    
    
    
    
    
