

import os
import sys

from crew import StoryWritingCrew
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file"""
    load_dotenv()
    
    # Check if Ollama is running (optional check)
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✓ Ollama is running and accessible")
        else:
            print("⚠️  Ollama might not be running. Please start Ollama service.")
    except:
        print("⚠️  Could not verify Ollama connection. Make sure Ollama is installed and running.")
        print("   Install Ollama from: https://ollama.ai/")
        print("   Then run: ollama serve")


def get_story_prompt():
    """Get story prompt from user input or use default"""
    print("Welcome to the AI Story Writing Crew!")
    print("=" * 50)
    
    # Default prompt
    default_prompt = "A short sci-fi story about a rogue AI discovering emotions"
    
    print(f"Default story prompt: '{default_prompt}'")
    print()
    
    user_input = input("Enter your own story prompt (or press Enter to use default): ").strip()
    
    if user_input:
        return user_input
    else:
        return default_prompt


def display_crew_info(crew):
    """Display information about the crew setup"""
    info = crew.get_crew_info()
    
    print("\nCrew Configuration:")
    print("=" * 30)
    print(f"Story Prompt: {info['story_prompt']}")
    print(f"Process: {info['process']}")
    print("\nAgents:")
    for i, agent in enumerate(info['agents'], 1):
        print(f"  {i}. {agent['role']}")
        print(f"     Goal: {agent['goal']}")
    
    print("\nTasks:")
    for i, task in enumerate(info['tasks'], 1):
        print(f"  {i}. {task['expected_output']}")
    
    print("\n" + "=" * 50)


def main():
    """Main execution function"""
    # Load environment variables
    load_environment()
    
    # Get story prompt
    story_prompt = get_story_prompt()
    
    # Get model preference
    model_name = os.getenv("OLLAMA_MODEL", "llama3.2")
    print(f"\nUsing Ollama model: {model_name}")
    
    # Create the crew
    print("\nInitializing Story Writing Crew...")
    crew = StoryWritingCrew(story_prompt=story_prompt)
    
    # Display crew information
    display_crew_info(crew)
    
    # Confirm execution
    print("The crew is ready to start writing your story!")
    confirm = input("Proceed with story creation? (y/n): ").strip().lower()
    
    if confirm not in ['y', 'yes']:
        print("Story creation cancelled.")
        return
    
    # Execute the story writing process
    try:
        print("\nStarting story writing process...")
        print("This may take several minutes depending on story complexity.")
        print()
        
        result = crew.write_story()
        
        print("\n" + "=" * 60)
        print("STORY WRITING COMPLETE!")
        print("=" * 60)
        print("\nFinal Result:")
        print("-" * 30)
        print(result)
        
        # Save result to file
        output_file = "generated_story.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(str(result))
        
        print(f"\nStory saved to: {output_file}")
        
    except Exception as e:
        print(f"\nError during story creation: {str(e)}")
        print("Please check that Ollama is running and the model is available.")
        print("Try running: ollama list")
        return


if __name__ == "__main__":
    main()
