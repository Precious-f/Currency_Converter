""" A currency convertor program  """

print('WELCOME!!!!')
#To take input of the users name
user_name =input('ENTER YOUR NAME: ')

#task is assigned the input of the user,either to make currency conversion or to exit the program
task=int(input(f'Hi {user_name}, How may I help you? \nEnter 1 to make a currency conversion \nEnter 2 to exit \n ->'))
if task == 1:
    #To take input of thr users country
    user_country = input(" SELECT THE COUNTRY YOU WORK IN ?\n A - NIGERIA \n B - UNITED STATE \n C - CANADA\n D - UNITED KINGDON\n E - CHINA\n F - SOUTH AFRICA\n G - GHANA \n H - FRANCE \n I - PAKISTAN\n J - JAPAN\n -> ")

    #To output the currency the user earn in 
    if user_country.lower() == 'a':
        print(f'{user_name}, you Earn in Naira')
    elif user_country.lower()  =='b':
        print(f'{user_name}, you Earn in Dollar')
    elif user_country.lower()  == 'c':
        print(f'{user_name}, you Earn in Canadian Dollar')    
    elif user_country.lower()  == 'd':
        print('You Earn in Pound ')  
    elif user_country.lower()  == 'e':
        print('You Earn in Chinese Yuan ') 
    elif user_country.lower()  == 'f':
        print('You Earn in  Rand') 
    elif user_country.lower()  == 'g':
        print('You Earn in Cedis') 
    elif user_country.lower()  == 'h':
        print('You Earn in Euro ') 
    elif user_country.lower()  == 'i':
        print('You Earn in Rupee') 
    elif user_country.lower()  == 'j':
        print('You Earn in Yen')   
    else :
        print('INVALID INPUT !!! \n')

    print('')

    

    Salary_convert=input('Would you like to convert your salary to another currency equivalence? (YES/NO) ')
    if Salary_convert.lower() == 'yes':

            x = 0
            while x == 0:
            

                print('GREAT!!! SELECT AN OPTION BELOW \n')
                currency_convert=input(' A - NAIRA to POUND \n B - NAIRA to DOLLAR \n C - NAIRA to EURO \n D - NAIRA to YEN \n E - NAIRA to RUPEE \n F - NAIRA to YUAN \n G - NAIRA to CEDIS \n H - NAIRA to RAND \n I - NAIRA to CANADIAN DOLLAR \n -> ')

                if currency_convert.lower() == 'a':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.00052)
                    print(f'-> £1 is equivalent to ₦1,907.67 \n\n->₦{amount} is equivalent to £{converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')


                elif currency_convert.lower() == 'b':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.00071)
                    print(f'-> $1 is equivalent to ₦1,363.71 \n\n->₦{amount} is equivalent to ${converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
                    
                    
                elif currency_convert.lower() == 'c':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.00066)
                    print(f'-> €1 is equivalent to ₦1,552.63 \n\n->₦{amount} is equivalent to €{converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
                    

                elif currency_convert.lower() == 'd':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.11)
                    print(f'-> ¥1 is equivalent to ₦9.35  \n\n->₦{amount} is equivalent to ¥{converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
                    

                elif currency_convert.lower() == 'e':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.059)
                    print(f'-> ₹1 is equivalent to ₦14.33 \n\n->₦{amount} is equivalent to ₹{converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
                    

                elif currency_convert.lower() == 'f':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.0052)
                    print(f'-> ¥1 is equivalent to ₦165.14 \n\n->₦{amount} is equivalent to ¥{converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
            

                elif currency_convert.lower() == 'g':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.010)
                    print(f'-> ¢1 is equivalent to ₦81.36\n\n->₦{amount} is equivalent to ¢{converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
                    

                elif currency_convert.lower() == 'h':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.013)
                    print(f'-> R1 is equivalent to ₦53.57 \n\n->₦{amount} is equivalent to R{converted_amount}') 
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')
                    
                elif currency_convert.lower() == 'i':
                    amount=int(input('Enter your salary or the amount you want to convert: '))
                    converted_amount= (amount*0.00098)
                    print(f'-> $1 is equivalent to ₦876.45 \n\n->₦{amount} is equivalent to ${converted_amount}')
                    print ('note that the exchange rate changes frequently and the values are apporixmated')
                    print('')
                    print ('I hope you are satisfied 😊')

                
                repeat = input('would you want to do another conversion? ')
                if repeat.lower() != 'yes':
                    x = x + 1
                    print(f' \nOkay {user_name} have a great day, feel free to chat me up whenever you need my help 😊')


            else:
                print('')

    elif Salary_convert=='no':
        print('Program stopped! ')
        print(f'Okay {user_name} have a great day, feel free to chat me up whenever you need my help 😊')

else:
    print(f'Okay {user_name} have a great day, feel free to chat me up whenever you need my help 😊')




