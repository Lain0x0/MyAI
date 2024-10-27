# My AI Web App

My AI is an interactive web application designed to assist users by providing answers to their questions using artificial intelligence. Built on a robust Flask backend and styled with Tailwind CSS, the app features a user-friendly interface that enhances accessibility.

## Key Features

- **AI-Powered Responses**: The app employs a sophisticated AI model to generate relevant content based on user queries.
- **Feedback Mechanism**: Users can provide feedback on the AI's responses, enabling continuous improvement and refinement of interactions.
- **Dark/Light Mode Toggle**: Users can easily switch between dark and light themes, allowing for a more personalized viewing experience.
- **Sensitive Topics Restriction**: The AI is programmed to avoid generating content on sensitive subjects such as politics, ethics, and morality, ensuring a safe and respectful interaction.

## Technologies Used

- **Frontend**: HTML, CSS (Tailwind CSS), JavaScript
- **Backend**: Python, Flask
- **AI Integration**: Google Gemini API
- **Development Tools**: Git for version control and Node.js for package management.

## Setup Instructions

To run the My AI web app locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/my-ai.git
   cd my-ai

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the server 'server.py':**
```bash
python3 / python server.py #Use python3 or python based on OS you use !
```

4. **Usage:**

- Open your web browser and navigate to http://localhost:3005.
- Enter your question in the input field and click "Submit" or press "Enter".
- Review the AI-generated response.
- Provide feedback on the response if desired.

5. **API Endpoints:**

POST /api

Description: Generates content based on the user's query.

Request Body:

```JSON
{
  "query": "Your question here"
}
```

Response:

```JSON
{
  "response": "AI-generated content",
  "response_id": "unique_id"
}
```

POST /feedback

Description: Submits feedback on the AI's response.

Request Body:

```JSON
{
  "feedback": "Your feedback here",
  "response_id": "response_id_here"
}
```

```JSON
{
  "message": "Feedback received. Thank you!"
}
```

**License:**

[MIT License](https://mit-license.org/)


**Author:**

Lain0x0 
[GitHub Profile](https://github.com/Lain0x0)
