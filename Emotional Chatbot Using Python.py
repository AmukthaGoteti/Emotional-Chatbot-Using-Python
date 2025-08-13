import re
import random
# Define patterns and responses for the chatbot
patterns = {
r'hi': ['Hello!'],

23 of 29

r'hello': ['Hi there!'],
r'hey': ['Hey!'],
r'how are you': ["I'm just a chatbot, but I'm here to help!", "I'm
here to provide support. How can I assist you today?"],
r'(.*) sad': ["I'm sorry to hear that. It's okay to feel down
sometimes. Would you like to talk about it?", "I'm here to listen.
What's been bothering you?"],
r'(.*) happy': ["That's great to hear!", "I'm glad to hear that
you're feeling happy. What's making you feel this way?"], r'(.*)
anxious': ["I understand that feeling. Let's work through it
together. What's been causing you stress or anxiety?"],
r'(.*) thank you': ["You're welcome!", "No problem at all. If you
have more questions or need support, feel free to ask."],
r'(.*) unhappy': ["I'm sorry to hear that. It's okay to feel down
sometimes. Would you like to talk about it?", "I'm here to listen.
What's been bothering you?"],
r'(.*) depressed': ["I'm sorry to hear that. It's okay to feel down
sometimes. Would you like to talk about it?", "I'm here to listen.
What's been bothering you?"],
r'(.*) down': ["I'm sorry to hear that. It's okay to feel down
sometimes. Would you like to talk about it?", "I'm here to listen.
What's been bothering you?"],
r'(.*) bad': ["I'm sorry to hear that. It's okay to feel down
sometimes. Would you like to talk about it?", "I'm here to listen.
What's been bothering you?"],
r'(.*) joyful': ["That's great to hear!", "I'm glad to hear that
you're feeling happy. What's making you feel this way?"], r'(.*)
good': ["That's great to hear!", "I'm glad to hear that you're
feeling happy. What's making you feel this way?"],
r'(.*) stressed': ["I understand that feeling. Let's work through it
together. What's been causing you stress or anxiety?"],
r'(.*) worried': ["I understand that feeling. Let's work through it
together. What's been causing you stress or anxiety?"],
r'bye': ['Goodbye!', 'Take care!', "If you ever need to talk, I'll be
here."],
r'goodbye': ['Goodbye!', 'Take care!', "If you ever need to talk,
I'll be here."],
r'(.*) help': ["Of course, I'm here to help. What do you need
assistance with?", "I'm ready to assist you. Please let me know what
you require help with."],
r'(.*) information': ["I can provide information on a wide range of
topics. Just let me know what you're interested in learning about."],
r'(.*) age': ["I'm just a computer program, so I don't have an age.
How can I assist you today?"],
r'(.*) hobby': ["I don't have hobbies, but I'm here to chat and
assist you with any questions or tasks."],
r'(.*) love': ["Love is a wonderful feeling. What would you like to
discuss or share about love today?"],
r'(.*) travel': ["Travelling is exciting! Where would you like to go
or share your travel experiences with me?"],
r'(.*) food': ["Food is a great topic! What's your favourite
cuisine?"],

24 of 29
r'(.*) Italian food': ["Italian cuisine is known for its delicious
pasta and pizza."],
r'(.*) Chinese food': ["Chinese food offers a wide range of
flavours."],
r'(.*) Mexican food': ["Mexican cuisine is famous for its vibrant
flavours."],
r'(.*) Indian food': ["Indian food is diverse and flavorful."],
r'(.*) Japanese food': ["Japanese cuisine is known for sushi, ramen,
and tempura."],
r'(.*) Thai food': ["Thai cuisine has a perfect blend of sweet, sour,
and spicy flavours."],
r'(.*) French food': ["French cuisine is renowned for its
elegance."],
r'(.*) hobbies': ["Hobbies are a fun way to spend your free time. Do
you have any hobbies or interests you'd like to discuss?"], r'(.*)
painting': ["Painting is a wonderful artistic hobby. Have you tried
painting, or are you interested in learning more about it?"],
r'(.*) photography': ["Photography is a creative way to capture
moments. Do you enjoy photography or want to learn more about it?"],
r'(.*) gardening': ["Gardening is a relaxing and rewarding hobby. Do
you have a green thumb, or are you curious about gardening tips?"],
r'(.*) cooking': ["Cooking can be a delightful hobby. Do you enjoy
cooking, or do you need any cooking tips or recipes?"], r'(.*)
reading': ["Reading is a fantastic way to escape into different
worlds. What kind of books do you like to read, or are you looking
for book recommendations?"],
r'(.*) music': ["Music is a wonderful form of expression. What's your
favourite genre or artist, or are you interested in learning to play
a musical instrument?"],
r'(.*) hiking': ["Hiking is a great way to connect with nature. Have
you been hiking recently, or are you looking for hiking trail
recommendations?"],
r'(.*) gaming': ["Gaming can be a fun pastime. Do you play video
games, board games, or other types of games?"],
r'(.*) sports': ["Sports can be a great way to stay active and have
fun. Are you a fan of any particular sport, or do you play any sports
yourself?"],
r'(.*) football': ["Soccer is a popular sport worldwide."],
r'(.*) basketball': ["Basketball is known for its fast-paced
action."], r'(.*) tennis': ["Tennis is a great sport for fitness."],
r'(.*) swimming': ["Swimming is a refreshing activity. Do you enjoy
swimming for leisure or fitness?"],
r'(.*) cycling': ["Cycling is an excellent way to explore and stay
fit. Do you like cycling or have any cycling adventures to share?"],
r'(.*) golf': ["Golf is a leisurely sport. Have you tried golfing or
watched golf tournaments?"],
r'(.*) baseball': ["Baseball is America's pastime. Are you a baseball
fan or ever played baseball?"],

r'(.*) martial arts': ["Martial arts offer self-discipline and self-
defence skills."],

r'(.*) volleyball': ["Volleyball is a fun team sport. Have you played
volleyball or watched volleyball matches?"],
r'(.*) cricket': ["Cricket is hugely popular in many countries."],

25 of 29
r'(.*) rugby': ["Rugby is a rugged sport."], r'(.*) art': ["Art is a
wonderful form of creativity."],
r'(.*) career advice': ["Planning your career path is crucial. How
can I assist you with career-related advice or information?"],
r'(.*) job': ["Finding the right job can be challenging.Job hunting
can be tough, but I'm here to assist. When searching for a job, it's
essential to start by identifying your skills and interests.
Networking is a valuable tool in the job search process. Consider
reaching out to your professional contacts and attending industry
events to expand your network. Online job boards, company websites,
and LinkedIn can be great resources for job listings. Have you tried
using these platforms for your job search?"],
r'(.*) interview': ["Interviews are a critical part of the job search
process. Interviews can be nerve-wracking, but with the right
preparation, you can excel. To excel in interviews, it's essential to
research the company, practise common interview questions, and dress
professionally. Successful interviews require a combination of
confidence and preparation."],
r'(.*) build a resume': ["Building a strong resume is the first step
toward landing your dream job. Here are some tips to get
started:\n\n1. Start with a clear and concise summary or objective
statement that highlights your career goals.\n2. List your work
experience in reverse chronological order, including your job titles,
company names, dates of employment, and key responsibilities.\n3.
Emphasise your achievements and accomplishments in each role, using
specific examples and quantifiable results.\n4. Include your
education, certifications, and relevant skills.\n5. Tailor your
resume to the specific job you're applying for by using keywords from
the job description.\n6. Keep your resume well-organised and easy to
read with clear headings and bullet points.\n7. Proofread for errors
in grammar and spelling."],
r'(.*) skills': ["Developing skills is important for career
advancement."],
r'(.*) education': ["Education plays a significant role in career
development."],
r'(.*) goals': ["Setting career goals can help you stay focused."],
r'(.*) work-life balance': ["Maintaining a healthy work-life balance
is crucial."],
}
# Create a function to respond to user input
def respond(user_input):
for pattern, responses in patterns.items():
match = re.match(pattern, user_input.lower())
if match:
return random.choice(responses)

return "I'm here to provide support. How can I assist you
today?"
# Define the main function
def main():
print("Emotional Support Chatbot: Hello! How can I assist you
today?")

26 of 29

print("Type 'goodbye' to end the conversation.")
while True:
user_input = input("You: ")
if user_input.lower() == 'goodbye':
print("Emotional Support Chatbot: Goodbye!")
break
response = respond(user_input)
print("Emotional Support Chatbot:", response)
if __name__ == "__main__": main()
