"""
Story Writing Crew

This module creates and manages the story-writing crew that coordinates
all agents and tasks for collaborative story creation.
"""

from crewai import Crew, Process
from agents import StoryWritingAgents
from tasks import StoryWritingTasks


class StoryWritingCrew:
    """Main crew class that orchestrates the story-writing process"""
    
    def __init__(self, story_prompt="A short sci-fi story about a rogue AI discovering emotions"):
        """
        Initialize the story-writing crew
        
        Args:
            story_prompt: The initial story concept or prompt
        """
        self.story_prompt = story_prompt
        
        # Initialize agents and tasks
        self.agents = StoryWritingAgents()
        self.tasks = StoryWritingTasks(story_prompt=story_prompt)
        
        # Create the crew
        self.crew = self._create_crew()
    
    def _create_crew(self):
        """Create the crew with agents and tasks"""
        # Get all agents
        agents_list = self.agents.get_all_agents()
        
        # Get tasks with assigned agents
        tasks_list = self.tasks.get_tasks_with_agents(agents_list)
        
        # Create the crew
        crew = Crew(
            agents=agents_list,
            tasks=tasks_list,
            process=Process.sequential,  # Sequential processing for story writing
            verbose=True
        )
        
        return crew
    
    def write_story(self):
        """
        Execute the story-writing process
        
        Returns:
            The final result from the crew execution
        """
        print(f"Starting story-writing process for: '{self.story_prompt}'")
        print("=" * 60)
        
        try:
            result = self.crew.kickoff()
            print("=" * 60)
            print("Story-writing process completed successfully!")
            return result
        except Exception as e:
            print(f"Error during story writing: {str(e)}")
            raise
    
    def get_crew_info(self):
        """Get information about the crew setup"""
        return {
            "story_prompt": self.story_prompt,
            "agents": [
                {
                    "role": agent.role,
                    "goal": agent.goal
                } for agent in self.agents.get_all_agents()
            ],
            "tasks": [
                {
                    "description": task.description[:100] + "..." if len(task.description) > 100 else task.description,
                    "expected_output": task.expected_output
                } for task in self.tasks.tasks
            ],
            "process": "Sequential"
        }
