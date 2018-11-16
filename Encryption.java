

public class Encryption
{
    String code;
    
    public Encryption(String theCode) //my constructor for the code. Intialising my varibale
    {
        code = theCode;
    }
    
    public String encryptedCode()
    {
    String finalCode = "";
    int[] characterArray = new int[code.length()]; //defining my array which will be the length of the string of the code 
    
    for (int i = 0; i < code.length(); i++){ //in this for loop my code will  
        int num = (int)(code.charAt(i));
        num = num + 1;
        characterArray[i] = num;

    }
    
    for(int i = 0; i < characterArray.length; i++)//for each loop that runs the loop for every element in the array. every element is equal to i 
    {
        char theChar = (char) characterArray[i];
        String theLetter = "" + theChar; //to string converts the character to a string 
        finalCode = finalCode + theLetter; //this concatnates the individual character length strings into one big string 
    
    
    
}
return finalCode;
}
}
