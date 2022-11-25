            #Queue Data Structure

    #Pointers
InitialPointer=-1;

    #container
container=[];

    #data storing functions
def pointerStatus() :
    Head=int;
    Tail=int;
    if len(container) == 0 :
        Head = Tail = InitialPointer;
        print('Head :',Head);
        print('Tail :',Tail);
    else :
        Head = 0;
        Tail = len(container)-1;
        print('Head :',Head);
        print('Tail :',Tail);
    return None;


def add(data) :
    #adding data
    container.append(data);
    print(data,' Added');
    return None;

def remove() :
    Head=int;
    Tail=int;
    if len(container) == 0 :
        Head = Tail = InitialPointer;
        print('Container Empty');
    else :
        Head = 0;
        Tail = len(container)-1;
        container.remove(container[Head]);
        Tail = Tail-1;
        print('Data removed');
    return None;

    #data entry


add('i');
add('r');
add('v');
add('i');
add('n');
add('g');
print('\n',container, '\n \n');



    #data searching

#convert to all uppercase
def convertUpper() :
    #pointers
    Head = 0;
    Tail = len(container)-1;
    UpperContainer = [];
    
    while len(container) > 0 :
        if container[Head].islower() == True :
            UpperContainer.append(container[Head].upper());
            container.remove(container[Head]);
        else :
            UpperContainer.append(container[Head]);
            container.remove(container[Head]);
    
    print('Converting lower case character to upper case : \n');
    print(UpperContainer);


    return None;

    
#execution

convertUpper();


#
        

