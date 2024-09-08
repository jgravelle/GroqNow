from pocketgroq import GroqProvider
import os
import sys

def clearscreen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def main():
    # Initialize the GroqProvider
    groq = GroqProvider()
    clearscreen()
    print("Welcome to the Simple Groq AI Chat!")
    print("Type 'exit' to end the conversation.")

    # Start the chat loop
    while True:
        # Get user input
        user_input = input("You: ").strip()

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")
            sys.exit(0)

        try:
            # Generate a response using Groq
            response = groq.generate(user_input)
            clearscreen()
            print("AI:", response)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
