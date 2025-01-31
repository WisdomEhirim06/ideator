# Ideator 

## Idea Generator App using Flask and OpenRouter API

## Overview
The Idea Generator App is a Flask-based web application that generates creative ideas based on predefined categories. By using the OpenRouter API and the Mistral AI model, the app serves a variety of unique ideas tailored to specific categories, such as startup ideas, weekend plans, writing prompts, challenges, and creative projects.

## Skills & Technologies Used
- **Backend Framework**: Flask
- **API Integration**: OpenRouter API
- **AI Model**: Mistral AI Model (via OpenRouter)
- **Environment Management**: Python `dotenv` for managing sensitive information
- **HTTP Requests**: `requests` library for interacting with the OpenRouter API
- **Frontend**: HTML (for rendering templates)

## AI Model: Mistral AI
This project uses the **Mistral AI** model from OpenRouter, designed for instruction-following tasks. Mistral's capabilities allow the app to generate human-like, context-specific ideas, making it an excellent choice for creative idea generation.

## Prompt Engineering: Crafting Ideas with Precision

### What is Prompt Engineering?
Prompt engineering is the art of designing inputs to guide AI models like Mistral in generating useful, creative, and contextually relevant outputs. In this project, we focused on crafting precise prompts that effectively guide the model to generate ideas based on specific categories.

### Techniques Used in the Project
To ensure the AI generates unique and engaging ideas, we used a **combination of prompting techniques**. These techniques helped refine the model's output and focused on creativity, clarity, and relevance. Here's how we applied each technique:

#### 1. **Framing Technique**
   - **What it is**: Framing refers to setting the context or boundaries for the model, ensuring the response aligns with the user's intent.
   - **How it was used**: For each category (startup ideas, weekend plans, etc.), we framed the prompt by providing clear guidelines on what the output should look like, such as the required tone, length, or specificity. For example, the prompt for *startup ideas* clearly defines what makes an idea innovative, feasible, and targeted at a specific market.

   Example from the *Startup Ideas* category:
   > "Generate an innovative and unique startup idea. The idea should solve a real problem, be technically feasible, and have a clear target market."

#### 2. **Interview Approach**
   - **What it is**: This technique treats the AI as a knowledgeable expert or consultant, asking it to respond with detailed, thoughtful insights as if answering an interview question.
   - **How it was used**: In the *weekend plans* category, we used a conversational approach to prompt the model to provide engaging, unconventional ideas, acting as though the model is helping to plan a fun weekend.

   Example from the *Weekend Plans* category:
   > "Create an unconventional and exciting weekend activity that could be done in 48 hours. The activity should be engaging and memorable, and include specific details relevant to Nigerians."

#### 3. **Zero-shot Prompting**
   - **What it is**: Zero-shot prompting involves giving the model a task without examples or training. The model is expected to generate an answer based on its pre-existing knowledge and understanding of the task.
   - **How it was used**: The AI was asked to generate ideas without any prior examples, simply using the instructions we provided in each category. This method encouraged the model to be more creative and generate ideas from scratch.

   Example from the *Writing Prompts* category:
   > "Craft a thought-provoking writing prompt that sparks creativity and is open to interpretation."

#### 4. **Direct Instruction Technique**
   - **What it is**: This technique involves giving the model clear, step-by-step instructions on how to produce the desired output. The instructions ensure that the model understands the key requirements and constraints.
   - **How it was used**: For categories like *creative projects*, we instructed the model to combine unexpected elements and provide clear steps, guiding it to produce practical yet imaginative ideas.

   Example from the *Creative Projects* category:
   > "Invent an imaginative creative project that combines unexpected elements, with clear steps, and results in a tangible output."

### How Prompt Engineering Affected the Project
Prompt engineering allowed us to shape the AI’s responses, ensuring that they were relevant to each category while maintaining creativity and specificity. By using techniques like framing, interview approach, and direct instructions, we were able to tailor the model’s output to generate ideas that were:
- **Engaging**: Each idea generated was interesting and engaging, tailored to the user’s needs.
- **Practical**: Ideas were actionable, with clear instructions for users to follow.
- **Human-like**: The language used in the responses was designed to sound natural and relatable, enhancing the overall user experience.

## Setting up the Project for Deployment

### Step 1: Install Dependencies
1. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
