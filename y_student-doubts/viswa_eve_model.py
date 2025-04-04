# Movie Chatbot: About "The Matrix"
print("Hello! I am a chatbot about the movie 'The Matrix'('director','release year',). Ask me anything, or type 'exit' to leave.")

while True:
        user_input = input("enter question: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! Feel free to come back anytime.")
            break
        elif "director" in user_input:
            print("Chatbot: 'The Matrix' was directed by the Wachowskis.")
        elif "release year" in user_input:
            print("Chatbot: 'The Matrix' was released in 1999.")
        elif "cast" in user_input:
            print("Chatbot: The main cast includes Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, and Hugo Weaving.")
        elif "plot" in user_input:
            print("Chatbot: 'The Matrix' is about a dystopian future where humanity is trapped in a simulated reality.")
        else:
            print("Chatbot: I'm sorry, I don't understand that. Try asking about the director, release year, cast, or plot!")
        
        continue_input = input("Chatbot: Do you want to know anything else? (yes/no): ").strip().lower()
        if continue_input == "no":
            print("Chatbot: Alright! Have a great day!")
            break
        elif continue_input != "yes":
             print("Chatbot: I'll take that as a yes. Let's continue!")