clc;
clear;
limit=210;
m=100;
sum=0;
i=1;
while ((i<=m)&&(sum<=limit))
  
        sum=sum+i;
            fprintf('sum at i=%2d is %d \n',i,sum)
        i=i+1;
end

    fprintf('\n\nFinally: sum = %3d for i=%2\n',sum,i)