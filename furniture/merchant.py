class Merchant:
    def __init__(self) -> None:
        self._name = 'merchant'
    
    def player_interaction(self, name):
        print(f'Hi {name} know who you are and what you want.') 
        print('And to recover your tresure you will need this shiny \033[94mblue key\033[0m')
        print('I am willing to give it to you, but you need to bring me the \033[0;35mSilver Necklace[0m')

    def __str__(self) -> str:
        return 'merchant'