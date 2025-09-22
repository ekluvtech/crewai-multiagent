#!/usr/bin/env python3
"""
Simple test script to verify Ollama connection and basic functionality
"""

import requests
from langchain_ollama import ChatOllama

def test_ollama_connection():
    """Test if Ollama is running and accessible"""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"✅ Ollama is running with {len(models)} models available:")
            for model in models[:3]:  # Show first 3 models
                print(f"  - {model.get('name', 'Unknown')}")
            return True
        else:
            print("❌ Ollama is not responding correctly")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to Ollama: {e}")
        return False

def test_langchain_ollama():
    """Test basic LangChain Ollama functionality"""
    try:
        # Create a simple ChatOllama instance
        llm = ChatOllama(
            model="llama3.2",
            temperature=0.7
        )
        
        # Test a simple completion
        print("\n🧪 Testing LangChain Ollama...")
        response = llm.invoke("Write a one-sentence story about a robot learning to dance.")
        print(f"✅ LangChain Ollama test successful!")
        print(f"Response: {response.content[:100]}...")
        return True
        
    except Exception as e:
        print(f"❌ LangChain Ollama test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🔍 Testing Story Writing Crew Setup")
    print("=" * 40)
    
    # Test Ollama connection
    if not test_ollama_connection():
        print("\n❌ Setup test failed. Please ensure Ollama is running.")
        return
    
    # Test LangChain Ollama
    if not test_langchain_ollama():
        print("\n❌ Setup test failed. Please check your Python environment.")
        return
    
    print("\n✅ All tests passed! Your setup is ready.")
    print("\nYou can now try running the full story writing crew:")
    print("  python3 main.py")

if __name__ == "__main__":
    main()
