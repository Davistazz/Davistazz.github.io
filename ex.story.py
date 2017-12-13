 # my story
greeting=input('Do you want to play? (yes/no)')

def first_choice():
    if greeting=='yes':
        print('Great...')
        response=input('Do you open the door? (yes/no)')
        second_choice(response)
    else:
        print('lame,bye then')

def second_choice(response):
    if response=="yes":
        which_door=input('Ok do you open the right or left door (left/right)')
        third_choice(which_door)
    else:
        print('lame, bye then')
        
def third_choice(which_door):
    if which_door=='left':
        print('You fall down a big hole in the ground and die')
    else:
        print('Surprise its your birthday') 

first_choice()
    



