
int digitNumber = 1;

int sum = 0;

int test = binary.length()%4;
 if(test!=0) {

binary = padLeft(binary' test);

}

for(int i = 0; i < binary.length(); i++){

if(digitNumber == 1) sum+=Integer.parseInt(binary.charAt(i) + "")*8;
 else if(digitNumber == 2) 
sum+=Integer.parseInt(binary.charAt(i) + "")*4; 
else if(digitNumber == 3) 
sum+=Integer.parseInt(binary.charAt(i) + "")*2;
else if(digitNumber == 4 II i < binary.length()+1)
{ 
sum+=Integer.parseInt(binary.charAt(i) + "")*1; 
digitNumber = 0;
if(sum < 10)
System.out.print(sum); 
else if(sum == 10) 
System.out.print("A"); 
else if(sum == 11)
System.out.print("B");

else if(sum == 12)
System.out.print("C"); 
else if(sum == 13)
System.out.print("D"); 
else if(sum == 14) 
System.out.print("E"); 
else
System.out.print("F"); 
sum=0;
}
digitNumber--;
}



