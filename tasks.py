"""
Story Writing Crew Tasks

This module defines the tasks for our story-writing crew, with proper dependencies
to ensure sequential execution: Plot → Characters → Scenes → Editing
"""

from crewai import Task


class StoryWritingTasks:
    """Container class for all story-writing tasks"""
    
    def __init__(self, story_prompt="A short sci-fi story about a rogue AI discovering emotions"):
        """
        Initialize tasks with a story prompt
        
        Args:
            story_prompt: The initial story concept or prompt
        """
        self.story_prompt = story_prompt
        self.tasks = self._create_tasks()
    
    def _create_tasks(self):
        """Create all tasks with proper dependencies"""
        tasks = []
        
        # Task 1: Plot Architecture
        plot_task = Task(
            description=f"""
            Create a comprehensive plot structure for the following story concept:
            "{self.story_prompt}"
            
            Your plot should include:
            1. A clear three-act structure (Setup, Confrontation, Resolution)
            2. Key plot points including inciting incident, midpoint, climax, and resolution
            3. Thematic elements and central conflict
            4. Story length and pacing considerations
            5. Target word count (aim for 1000-2000 words for a short story)
            
            Format your response as a structured plot outline with:
            - Story premise and theme
            - Act-by-act breakdown
            - Key scenes and plot points
            - Character needs (what characters are required)
            """,
            expected_output="A detailed plot structure with three-act breakdown, key plot points, themes, and character requirements",
            agent=None,  # Will be assigned when creating the crew
            output_file="plot_structure.txt"
        )
        
        # Task 2: Character Development
        character_task = Task(
            description="""
            Based on the plot structure created by the Plot Architect, develop the main characters for this story.
            
            For each main character, create:
            1. Name, age, and basic physical description
            2. Core personality traits and motivations
            3. Internal and external conflicts
            4. Character arc (how they change throughout the story)
            5. Relationships with other characters
            6. Dialogue style and voice
            
            Focus on creating 2-3 main characters maximum for a short story.
            Ensure characters serve the plot and thematic elements.
            """,
            expected_output="Detailed character profiles for all main characters including backgrounds, motivations, conflicts, and arcs",
            agent=None,  # Will be assigned when creating the crew
            context=[plot_task],  # Depends on plot structure
            output_file="character_profiles.txt"
        )
        
        # Task 3: Scene Writing
        scene_task = Task(
            description="""
            Using the plot structure and character profiles, write the complete short story.
            
            Your story should:
            1. Follow the three-act structure outlined in the plot
            2. Feature the developed characters with their unique voices
            3. Include vivid descriptions and engaging dialogue
            4. Maintain consistent pacing and tension
            5. Be approximately 1000-2000 words
            6. Have a clear beginning, middle, and end
            7. Resolve the central conflict satisfactorily
            
            Write the complete story in a single, polished draft.
            """,
            expected_output="A complete short story (1000-2000 words) following the plot structure and featuring the developed characters",
            agent=None,  # Will be assigned when creating the crew
            context=[plot_task, character_task],  # Depends on both plot and characters
            output_file="story_draft.txt"
        )
        
        # Task 4: Narrative Editing
        editing_task = Task(
            description="""
            Review and edit the completed story for:
            
            1. Narrative coherence and flow
            2. Character consistency and voice
            3. Plot pacing and structure
            4. Dialogue quality and authenticity
            5. Description vividness and clarity
            6. Thematic consistency
            7. Grammar, punctuation, and style
            8. Overall impact and emotional resonance
            
            Provide both:
            - A revised version of the story
            - A brief editorial report highlighting changes made and why
            
            Ensure the final story is polished and ready for publication.
            """,
            expected_output="A polished final story and editorial report detailing improvements made",
            agent=None,  # Will be assigned when creating the crew
            context=[plot_task, character_task, scene_task],  # Depends on all previous tasks
            output_file="final_story.txt"
        )
        
        return [plot_task, character_task, scene_task, editing_task]
    
    def get_tasks_with_agents(self, agents):
        """Assign agents to tasks and return the complete task list"""
        if len(agents) != 4:
            raise ValueError("Expected exactly 4 agents for the story-writing crew")
        
        plot_architect, character_crafter, scene_weaver, narrative_editor = agents
        
        # Assign agents to their respective tasks
        self.tasks[0].agent = plot_architect
        self.tasks[1].agent = character_crafter
        self.tasks[2].agent = scene_weaver
        self.tasks[3].agent = narrative_editor
        
        return self.tasks
