a=rand(3,4);
b=a(1,2);
clc;
x=[45 23 17;34 85 33];
[row,col]= size (x);
num=0;
for i=1:row
    for j=1:col
        if (x(i,j)<30)
         fprintf('X(%1d,%1d)=%2d<30\n',i,j,x(i,j))      
            num=num+1;
        end
        
    end
end  
   fprintf('\n\nFinally: Number of elements less than 30 is %d\n',num)