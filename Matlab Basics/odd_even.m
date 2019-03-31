A=reshape(1:20,4,5);
for i=1:5
    for j=1:4
        a=A(j,i);
        if   (rem(a,2)==0) 
            fprintf('A(%2d,%2d)=%2d is even\n',j,i,a)
        else 
            fprintf('A(%2d,%2d)=%2d is odd\n',j,i,a)
        end
    end
end
