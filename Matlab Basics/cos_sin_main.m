pi=3.14;
for i=0:pi/6:pi*2
   x=(i*180)/pi; 
   co=cosd(x);
   si=sind(x);
    fprintf('cos(%3.0f)= %3.3f & sin(%3f)= %3.3f \n',x,co,x,si)
end