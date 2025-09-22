"""
Example usage of the Story Writing Crew

This script demonstrates different ways to use the crew for various story types.
"""

from crew import StoryWritingCrew
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def example_sci_fi_story():
    """Example: Create a sci-fi story about AI discovering emotions"""
    print("Example 1: Sci-Fi Story")
    print("=" * 40)
    
    crew = StoryWritingCrew(
        story_prompt="A short sci-fi story about a rogue AI discovering emotions"
    )
    
    result = crew.write_story()
    print("Story completed!")
    return result


def example_fantasy_story():
    """Example: Create a fantasy story"""
    print("Example 2: Fantasy Story")
    print("=" * 40)
    
    crew = StoryWritingCrew(
        story_prompt="A fantasy story about a young mage who must choose between power and love"
    )
    
    result = crew.write_story()
    print("Story completed!")
    return result


def example_mystery_story():
    """Example: Create a mystery story"""
    print("Example 3: Mystery Story")
    print("=" * 40)
    
    crew = StoryWritingCrew(
        story_prompt="A detective story set in 1920s Paris involving a stolen painting and secret society"
    )
    
    result = crew.write_story()
    print("Story completed!")
    return result


def main():
    """Run example stories"""
    # Check if Ollama is running
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code != 200:
            print("Error: Ollama is not running. Please start Ollama service.")
            return
    except:
        print("Error: Cannot connect to Ollama. Please install and start Ollama.")
        return
    
    print("Story Writing Crew Examples")
    print("=" * 50)
    print("Choose an example to run:")
    print("1. Sci-Fi Story (AI discovering emotions)")
    print("2. Fantasy Story (mage choosing between power and love)")
    print("3. Mystery Story (1920s Paris detective)")
    print("4. Run all examples")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        example_sci_fi_story()
    elif choice == "2":
        example_fantasy_story()
    elif choice == "3":
        example_mystery_story()
    elif choice == "4":
        print("Running all examples...")
        example_sci_fi_story()
        print("\n")
        example_fantasy_story()
        print("\n")
        example_mystery_story()
    elif choice == "5":
        print("Goodbye!")
    else:
        print("Invalid choice. Please run the script again.")


if __name__ == "__main__":
    main()
