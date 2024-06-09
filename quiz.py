Questions={
    "History":{
        "easy":[
            {"question":"When did India get independence?","answer":"1947"},
            {"question":"Who is the first prime minister of India?","answer":"Jawaharlal Nehru"},
            {"question":"Who is known as the father of the nation of India?","answer":"Mahatma Gandhi"}
        ],
        "medium":[
            {"question":"Who is the first person to go to Space?","answer":"Yuri Gagarin"},
            {"question":"Who is the first Indian to go to Space?","answer":"Rakesh Sharma"},
            {"question":"Who discovered America?","answer":"Christopher columbus"}
        ],
        "hard":[
            {"question":"In which battle did Napoleon lose?","answer":"Battle of Waterloo"},
            {"question":"When did the french revolution take place?","answer":"1789-1799"},
            {"question":"Who is called the iron man of the world?","answer":"Otto von Bismarck"}
        ]
    },
    "Biology":{
        "easy":[
            {"question":"What is called the power house of a cell?","answer":"Mitochondria"},
            {"question":"What is the process thorugh which plants prepare food?","answer":"Photosynthesis"},
            {"question":"How many sense organs are there in the human body?","answer":"5"}
        ],
        "medium":[
            {"question":"Who discovered pencillin?","answer":"Alexander fleming"},
            {"question":"Who proposed the theory of evolution?","answer":"Charles darwin"},
            {"question":"What causes malaria?","answer":"Protozoa"}
        ],
        "hard":[
            {"question":"What are the sites for protein synthesis?","answer":"Ribosomes"},
            {"question":"Which are called the suicidal bags of the cell?","answer":"Lysosomes"},
            {"question":"Which vitamin helps in blood clotting?","answer":"Vitamin K"}
        ]
    }
}
def Ques(question):
    print(question["question"])
    initial=input("type the answer here: ").strip()
    if initial.lower()==question["answer"].lower():
        print("You are correct")
        return True
    else:
        print("You are wrong...")
        return False
def subject():
    while True:
        sub=input("History or Biology:").strip()
        if sub in Questions:
            return sub
        else:
            print("subject doesn't exist......")
def choose_mode():
    while True:
        mode=input("choose your mode: ").strip().lower()
        if mode in ["easy","medium","hard"]:
            return mode
        else:
            print("Mode as such is unavailable......")

def play():
    print("----------Welcome to the Quiz Game!!!--------------")
    sub=subject()
    mode=choose_mode()
    List=Questions[sub][mode]
    score=0
    for question in List:
        if Ques(question):
            score+=1
    print("-----The results------")
    print(f"You have received {score} marks in this quiz.....")

play()