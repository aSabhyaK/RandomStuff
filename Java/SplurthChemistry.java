/*
link for the challenge:
https://dzone.com/articles/java-code-challenge-chemical-symbol-naming-part-on?utm_source=java%20code%20challenge&utm_medium=emaiol&utm_campaign=jcc%202016-08-08
*/

import java.util.Map;
import java.util.HashMap;
import java.util.TreeMap;

public class SplurthChemistry
{
  public static void main(String[] args)
  {
    String[] chemicalNameArray = {"Spenglerium", "Zeddemorium", "Venkmine", "Stantzon", "Melintzum", "Tullium", "Boron", "Mercury"};
    String[] chemicalSymbolArray = {"Ee", "Zr", "Kn", "Zt", "Nn", "Ty", "B", "Hg"};
    
    int size = chemicalNameArray.length;
    
    for(int i = 0; i < size; ++ i)
      System.out.println(chemicalNameArray[i] 
                         + "(" 
                         + firstInAlphabeticalOrderSymbol(chemicalNameArray[i].toLowerCase()) 
                         + ") and " 
                         + chemicalSymbolArray[i] 
                         + ": " 
                         + checkIt(chemicalNameArray[i].toLowerCase(), chemicalSymbolArray[i].toLowerCase()));
  }
  
  private static String firstInAlphabeticalOrderSymbol(String name)
  {
    TreeMap<Character, Integer> map = new TreeMap<>();
    
    for(char c: name.toCharArray())
    {
		if(map.containsKey(c))
          map.put(c, map.get(c) + 1);
      
      	else
          map.put(c, 1);
    }
    
    StringBuilder stringBuilder = new StringBuilder();
    
    int counter = 0;
    for(Character character: map.keySet())
    {
    	if(counter == 2)
          break;
      
      	if(map.get(character) == 2 && stringBuilder.toString().isEmpty())
        {
        	stringBuilder.append(character).append(character);
          	break;
        }
      
      	else{
      		stringBuilder.append(character);
        }
          
      	counter ++;
    }
    
  	return stringBuilder.toString();
  }
  
  private static boolean checkIt(String name, String symbol)
  {
    if(condition1(name, symbol) && condition2(name, symbol) && condition3(name, symbol) || condition4(name, symbol))
    	return true;
    
    return false;
  }
  
  private static boolean condition1(String name, String symbol)
  {
    /*
    1. All chemical symbols must be exactly two letters, so B is not a valid symbol for Boron.
    */
  	return symbol.length() == 2;
  }
  
  private static boolean condition2(String name, String symbol)
  {
    /*
    2. Both letters in the symbol must appear in the element name, but the first letter of the 
    	element name does not necessarily need to appear in the symbol. 
        So Hg is not valid for Mercury, but Cy is.
    */
    String[] array = symbol.split("");
  	return name.indexOf(array[0]) != -1 && name.indexOf(array[1]) != -1;
  }
  
  private static boolean condition3(String name, String symbol)
  {
    /*
    3. The two letters must appear in order in the element name. So Vr is valid for Silver, 
    	but Rv is not. To be clear, both Ma and Am are valid for Magnesium, because there is 
        both an a that appears after an m, and an m that appears after an a.
    */
    String[] array = symbol.split("");
    int indexOfFirstCharacter = name.indexOf(array[0]);
    
    if(indexOfFirstCharacter == -1)
      return false;
    
    int lengthOfName = name.length();
    
    for(int i = indexOfFirstCharacter + 1; i < lengthOfName; ++ i)
    {
    	if(name.charAt(i) == array[1].charAt(0))
          return true;
    }
    
  	return false;
  }
  
  private static boolean condition4(String name, String symbol)
  {
    /*
    4. If the two letters in the symbol are the same, it must appear twice in the element name. 
    	So Nn is valid for Xenon, but Xx and Oo are not.
    */
    Map<Character, Integer> nameMap = new HashMap<>();
    Map<Character, Integer> symbolMap = new HashMap<>();
    
    for(char c: name.toCharArray())
    {
    	if(nameMap.containsKey(c))
          nameMap.put(c, nameMap.get(c) + 1);
      
      	else
          nameMap.put(c, 1);
    }
    
    for(char d: symbol.toCharArray())
    {
    	if(symbolMap.containsKey(d))
          symbolMap.put(d, symbolMap.get(d) + 1);
      
      	else
          symbolMap.put(d, 1);
    }
    
    if(symbolMap.size() != 1)
      return false;
    
    char selectedKey = '\0';
    
    for(Character character: symbolMap.keySet())
    	selectedKey = character;
    
    return nameMap.get(selectedKey) == 2;
  }
}
