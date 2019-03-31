n=20;
counter =1
while n~=1
    if rem(counter,2)==0
        n=n/2;
    else
        n=n/4;
    end
counter = counter+1;
end
