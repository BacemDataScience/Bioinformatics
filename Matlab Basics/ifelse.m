prompt='what is the original value?' ;
x=input(prompt)
if x>=0
y=sqrt (x)
else y=0
end

prompt='what is x?' ;
x=input(prompt)
if x>=0 
y=x^(0.5)
elseif x<0
y=exp(x)-1
end