"""
Story Writing Crew Agents

This module defines the four specialized agents for our story-writing crew:
1. Plot Architect - Designs the overall story structure and plot
2. Character Crafter - Develops characters with motivations and arcs
3. Scene Weaver - Writes actual scenes integrating plot and characters
4. Narrative Editor - Reviews and refines for coherence and polish
"""

from crewai import Agent
from langchain_ollama import ChatOllama
from config import *

class StoryWritingAgents:
    """Container class for all story-writing agents"""
    
    def __init__(self):
        """
        Initialize agents with Ollama LLM
        
        Args:
            model_name: Ollama model name to use (defaults to llama3.2)
        """
        self.llm = ChatOllama(
            model=LLM_MODEL,
            temperature=0.7,
            base_url=OLLAMA_URL
        )
        
        self.plot_architect = self._create_plot_architect()
        self.character_crafter = self._create_character_crafter()
        self.scene_weaver = self._create_scene_weaver()
        self.narrative_editor = self._create_narrative_editor()
    
    def _create_plot_architect(self):
        """Create the Plot Architect agent"""
        return Agent(
            role="Plot Architect",
            goal="Design compelling story structures with clear narrative arcs, plot points, and thematic elements",
            backstory="""You are a master storyteller with decades of experience in crafting 
            compelling narratives. You specialize in creating intricate plot structures that 
            engage readers from beginning to end. Your expertise lies in developing three-act 
            structures, character-driven plots, and thematic coherence. You understand how to 
            balance pacing, tension, and resolution to create emotionally satisfying stories.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def _create_character_crafter(self):
        """Create the Character Crafter agent"""
        return Agent(
            role="Character Crafter",
            goal="Develop rich, multi-dimensional characters with clear motivations, flaws, and growth arcs",
            backstory="""You are a character development specialist with a deep understanding 
            of human psychology and storytelling. You excel at creating characters that feel 
            real and relatable, with complex inner lives and believable motivations. Your 
            characters drive the plot forward through their desires, fears, and relationships. 
            You understand how character arcs intersect with plot development to create 
            emotionally resonant narratives.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def _create_scene_weaver(self):
        """Create the Scene Weaver agent"""
        return Agent(
            role="Scene Weaver",
            goal="Write engaging, vivid scenes that bring the plot and characters to life through dialogue, action, and description",
            backstory="""You are a master of scene writing with exceptional skill in crafting 
            immersive, engaging prose. You excel at balancing dialogue, action, and description 
            to create scenes that advance the plot while developing characters. Your writing 
            is vivid and emotionally compelling, drawing readers into the world of the story. 
            You understand pacing, tension, and the importance of showing rather than telling.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def _create_narrative_editor(self):
        """Create the Narrative Editor agent"""
        return Agent(
            role="Narrative Editor",
            goal="Review and refine the story for coherence, pacing, flow, and overall narrative quality",
            backstory="""You are an experienced editor with a keen eye for story structure, 
            pacing, and narrative flow. You excel at identifying inconsistencies, plot holes, 
            and areas where the story can be strengthened. Your expertise lies in ensuring 
            thematic coherence, character consistency, and smooth transitions between scenes. 
            You polish prose while maintaining the author's voice and vision.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
    
    def get_all_agents(self):
        """Return all agents as a list"""
        return [
            self.plot_architect,
            self.character_crafter,
            self.scene_weaver,
            self.narrative_editor
        ]
