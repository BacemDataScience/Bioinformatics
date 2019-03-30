import java.util.Scanner;

public class CompressString {

public static void main(StringlJ args) { 
Scanner sc = new Scanner(System.in); 
System.out.print("Enter string:  "); 
String str = sc.nextLine(); 
System.out.println("lnput:  " + str);
 String compressed = "";

char ch=O;
int count=1;

for (int x = O; x < str.length(); x++)
	{

if (ch == str.charAt(x)){

count = count + 1;

} 
else {

compressed = compressed + ch;

if(count != 1){

compressed = compressed + count;

}

ch = str.charAt(x);

count = 1;

}

}

compressed = compressed + ch;

if(count != 1){

compressed = compressed - count;

}

System.out.println("Compressed:  " - compressed);

}

}

