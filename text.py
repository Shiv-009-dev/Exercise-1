questions = [
    ["1)what is the capital of india?" , "Mumbai" , "New Delhi" , "Bihar" , "Uttar Pradesh" , 2] , 
    ["2)who is the current prime minister of india?" , "Manmohan Singh" , "Atal Bihari Vajpayee" , "Narendra Modi" , "Rajendra Prasad", 3 ] , 
    ["3)what is currency of india?" , "Rupee" , "Dollar" , "Pound" , "Euro" , 1 ] , 
    ["4)who is the current president of india?" , "Pranab Mukherjee" , "Ram Nath Kovind" , "Rajendra Prasad" , "Draupadi Murmu" , 4 ] , 
    ["5)where is india's silicon valley located?" , "Gujrat" , "Mumbai" , "Uttar Pradesh" , "Bangalore" , 4 ] , 
    ["6)when was india's independence day?" , "5Sep" , "26Jan" , "15Aug" , "23July" , 3 ] , 
]

levels = [25000 , 50000 , 100000 , 200000 , 400000 , 800000]

for i in range(0,len(questions)):
    question = questions[i]
    print(f"\n\n{question[0]}\n Question for Rs. {levels[i]}")
    print(f"A.{question[1]}\nB.{question[2]}\nC.{question[3]}\nD.{question[4]}")
    reply = int(input("#Enter your answer(plz enter your ans in numbers 1 to 4) :"))
    if(reply == question[-1]):
        print(f"Correct answer , you have won Rs. {levels[i]}")
    else:
        print("Wrong answer!")
        break
