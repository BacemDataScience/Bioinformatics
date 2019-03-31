fun=zeros(1,25);
i=1;
max_val=-9999;
for x=-6:0.5:6
    if (x<0)
        fun(i)=exp(cos(x))-2*cos(4*x)-(sin(x/12))^5;
    else
        fun(i)=exp(sin(x))-2*sin(4*x)-(cos(x/12))^5;
    end
    if(fun(i)>max_val)
    max_val=fun(i)        
    end
    i=i+1;
end
