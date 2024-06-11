Questions={
    "History":{
        "easy":[
            {"question":"When did India get independence? A.1950 B.1947 C.1981 D.1946","answer":"B"},
            {"question":"Who is the first prime minister of India? A.Jawaharlal nehru B.Rajendra Prasad C.Gandhi D.BG Tilak","answer":"A"},
            {"question":"Who is known as the father of the nation of India? A.Shivaji B.Mahatma Gandhi C.Rajiv gandhi D.Subhash chadra bose","answer":"B"}
        ],
        "medium":[
            {"question":"Who is the first person to go to Space? A.Laika B.Neil Armstrong C.Rakesh Sharma D.Yuri Gagarin","answer":"D"},
            {"question":"Who is the first Indian to go to Space? A.Sunitha williams B.Kalpana Chawla C.Rakesh Sharma D.Yuri Gagarin","answer":"C"},
            {"question":"Who discovered America? A.MarcoPolo B.Vincent Van goh C.Galileo D.Christopher columbus","answer":"D"}
        ],
        "hard":[
            {"question":"In which battle did Napoleon lose? A.BLood Battle B.Battle of Waterloo C.Battle of strengths D.Sussex Battle","answer":"B"},
            {"question":"When did the french revolution start? A.1589 B.1689 C.1789 D.1889","answer":"C"},
            {"question":"Who is called the iron man of the world? A.Mussolini B.Napoleon C.Adolf Hitler D.Otto von bismarck","answer":"D"}
        ]
    },
    "Biology":{
        "easy":[
            {"question":"What is called the power house of a cell? A.Vacuole B.Membrane C.Ribosomes D.Mitochondria","answer":"D"},
            {"question":"What is the process thorugh which plants prepare food? A.Respiration B.Transpiration C.Evaporation D.Photosynthesis","answer":"D"},
            {"question":"How many sense organs are there in the human body? A.5 B.2 C.4 D.6","answer":"A"}
        ],
        "medium":[
            {"question":"Who discovered pencillin? A.Charles Darwin B.Von Sachs C.Robert Hooke D.Alexander Fleming","answer":"D"},
            {"question":"Who proposed the theory of evolution? A.Vincent Chansard B.Louis Pasteur C.Charles Darwin D.Aristotle","answer":"C"},
            {"question":"What causes malaria? A.Bacteria B.Protozoa C.Virus D.Pigs","answer":"B"}
        ],
        "hard":[
            {"question":"What are the sites for protein synthesis? A.Lungs B.Bronchi C.Blood Cells D.Ribosomes","answer":"D"},
            {"question":"Which are called the suicidal bags of the cell? A.Lysosomes B.Amoeba C.Mitochondria D.Vacuole","answer":"A"},
            {"question":"Which vitamin helps in blood clotting? A.Vitamin D B.Vitamin A C.Vitamin K D.Vitamin B","answer":"C"}
        ]
    }
}
def Ques(question):
    print(question["question"])
    initial=input("The Option is: ").strip()
    if initial.upper()==question["answer"].upper():
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
            print("Subject doesn't exist......")
def choose_mode():
    while True:
        mode=input("Choose your mode (easy/medium/hard): ").strip().lower()
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