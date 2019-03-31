prompt='what is the initial position' ;
p=input(prompt)
prompt = 'Do you want S/M?';
str= input(prompt,'s');
t=-1;size=-1;
if str=='s'
        while(t<=0)
        prompt='what is t' ;
        t=input(prompt);
        end  
else
        while(size<=0)
        prompt='what is l of M' ;
        l=input(prompt);
        end  
    
end