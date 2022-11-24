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


add('a');
add('l');
add('i');

    #data searching


#
        

