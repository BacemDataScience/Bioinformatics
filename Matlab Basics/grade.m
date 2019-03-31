A= cell([8,4]);
for i=1:3
 if (i==1)
    for j= 1:8
    A{j,i}=input('n° :');
    end
 end
  if (i==2)
    for j= 1:8
    A{j,i}=input('Name :','s');
    end
  end
   if (i==3)
    for j= 1:8
    A{j,i}=input('grade :');
    end
   end
    
end
for (i=1:8)
    if (A{i,3}<60)
     A{i,4}='Fail';
    elseif (A{i,3}<70)
     A{i,4}='Fair';
    elseif (A{i,3}<80)
     A{i,4}='Good';
      elseif (A{i,3}<90)
     A{i,4}='V. Good';
    elseif   (A{i,3}<=100)
     A{i,4}='Exc.';
    else 
          A{i,4}='God mode';
    end
end
     