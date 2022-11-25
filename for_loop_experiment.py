#for loop learning

x = [];
for i in range(1,6) :
    i=input('insert number here :');
    i=int(i);
    x.append(i);

print(x);

#
y=[];
pointer=0;
status=bool;
for element in x :
    if x[pointer] > 2 :
        status=True;
        y.append(status);
        pointer = pointer+1;
    else :
        status=False;
        y.append(status);
        pointer=pointer+1;

print(y);


