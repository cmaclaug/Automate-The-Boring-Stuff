print ('What is your name?')
name = input()
print ('What is your age?')       
age = input()
if (name == 'Alice' or name == 'alice') and (int(age) >= 12 and int(age) <= 100):
    print ('Hi Alice')
elif int(age) < 12 and (name != 'Alice' and name != 'alice'):
    print ('You are not Alice, kiddo.')
elif int(age) > 2000 and (name != 'Alice' and name != 'alice'):
    print ('Unlike you, Alice is not an undead, immortal vampire')
elif int(age) > 100 and (name != 'Alice' and name != 'alice'):
    print ('You are not Alice, grannie')


    

    
