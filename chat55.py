import google.generativeai as ai

# Configuration
API_KEY = "AIzaSyCa61z0V5Rlx0itheCoPf9nwul_JkvYlJY"

def configure_ai(api_key):
    """Configures the Generative AI client."""
    try:
        ai.configure(api_key=api_key)
    except Exception as e:
        print(f"Error configuring the AI client: {e}")
        raise

# Initialize the model and chat instance
def initialize_chat(model_name="gemini-pro"):
    """
    Initializes the chatbot model and returns a chat instance.
    
    Args:
        model_name (str): The name of the model to use.
    
    Returns:
        chat_instance: The initialized chat instance.
    """
    try:
        model = ai.GenerativeModel(model_name)
        return model.start_chat()
    except Exception as e:
        print(f"Error initializing the model: {e}")
        return None

# Main chat function
def chat_with_model(chat_instance):
    """
    Facilitates conversation with the chatbot.
    
    Args:
        chat_instance: The initialized chat instance.
    """
    if not chat_instance:
        print("Chatbot initialization failed. Exiting...")
        return

    print("Chatbot is ready! Type 'bye' to exit.")
    while True:
        try:
            # User input
            user_message = input("You: ").strip()
            if not user_message:  # Skip empty input
                print("Chatbot: Please say something.")
                continue
            if user_message.lower() == "bye":  # Exit condition
                print("Chatbot: Goodbye!")
                break
            
            # Get response from the chatbot
            response = chat_instance.send_message(user_message)
            print("Chatbot:", response.text)
        except Exception as e:
            print(f"Error during conversation: {e}")
            break

# Main execution
if __name__ == "__main__":
    try:
        configure_ai(API_KEY)  # Configure AI with API Key
        chat_instance = initialize_chat()  # Initialize chat
        chat_with_model(chat_instance)  # Start chat session
    except Exception as main_error:
        print(f"An error occurred: {main_error}")
