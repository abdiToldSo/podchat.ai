from google import genai
import os

# Configure the API key (replace with your actual API key or environment variable)
genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

class GeminiInteraction:
    def __init__(self, model_name="gemini-pro"):
        """Initializes the GeminiInteraction class with a specified model."""
        self.model = genai.GenerativeModel(model_name)

    def generate_text(self, prompt):
        """Generates text based on the given prompt using the Gemini API."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating text: {e}"

    def generate_text_with_options(self, prompt, generation_config=None, safety_settings=None):
        """Generates text with custom generation and safety settings."""
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config,
                safety_settings=safety_settings
            )
            return response.text
        except Exception as e:
            return f"Error generating text: {e}"

# Example usage:
if __name__ == "__main__":
    # Ensure you have your GOOGLE_API_KEY environment variable set
    if "GOOGLE_API_KEY" not in os.environ:
        print("Please set the GOOGLE_API_KEY environment variable.")
    else:
        gemini_interactor = GeminiInteraction()
        user_prompt = "Write a short poem about a blooming flower."
        generated_poem = gemini_interactor.generate_text(user_prompt)

        if generated_poem:
            print("Generated Poem:")
            print(generated_poem)

        # Example with custom generation configuration
        custom_config = genai.types.GenerationConfig(
            temperature=0.9,
            top_p=0.8,
            top_k=40,
            max_output_tokens=256
        )
        custom_poem = gemini_interactor.generate_text_with_options(
            user_prompt, generation_config=custom_config
        )
        if custom_poem:
            print("\nGenerated Poem with Custom Configuration:")
            print(custom_poem)
