from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from .crawler import scrape_website
import json

import os
cwd = os.getcwd()

json_file_path = cwd + '/data/parsed_data.json'

# Load the JSON data
with open(json_file_path, 'r') as file:
    parsed_data = json.load(file)

class GenerateResponseAction(Action):
    def name(self):
        return "action_generate_response"

    async def run(self, dispatcher, tracker, domain):
        # Extract user intent, user input, and related product information from the conversation tracker
        user_intent = tracker.latest_message.get("intent").get("name")
        user_input = tracker.latest_message.get("text")
        url = "https://docs.zowe.org/stable/web_help/index.html?p=zowe_config_edit&v=1" # zowe command tree (flat view)
        related_info = await self.get_related_product_info(url,tracker.get_slot("search_query"), parsed_data)
        # Load GPT-2 model and tokenizer
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

        # Construct a prompt based on intent, user input, and related information
        prompt = f"Intent: {user_intent}\nUser Input: {user_input}\nproduct Info: {related_info}\n"

        # Generate a response using GPT-2
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # send the response to the user in the ongoing conversation
        dispatcher.utter_message(response)

        return [SlotSet("generated_response", response)]  # stores the generated response for future reference

    async def get_related_product_info(self, url, search_query, parsed_data):
        # Call scrape_website with the URL and search query
        url = "https://docs.zowe.org/stable/web_help/index.html?p=zowe_config_edit&v=1"
        scraped_info = await scrape_website(url, search_query)

        # Initialize a list to store relevant sections and subsections
        relevant_sections = []

        for section in parsed_data:
            if search_query in section:
                # If the keyword is found in the section, add the section itself
                relevant_sections.append(section)

                # Check if the section contains subsections
                if isinstance(parsed_data[section], list):
                    # If it does, add all those subsections to the relevant sections
                    relevant_sections.extend(parsed_data[section])

        # Format the relevant product information
        relevant_info = "\n".join(relevant_sections) + "\n".join(scraped_info)

        return relevant_info

class DetermineQueryAction(Action):
    def name(self):
        return "action_determine_query"

    async def run(self, dispatcher, tracker, domain):
        # Check if the search query has already been extracted
        search_query = tracker.get_slot("search_query")

        if not search_query:
            # If the search query is not provided, use GPT-2 to determine it
            user_message = tracker.latest_message.get("text")
            generated_query = await self.generate_query_with_gpt2(user_message)

            if generated_query:
                dispatcher.utter_message(f"I believe your query is: {generated_query}") #TO DELETE
                return [SlotSet("search_query", generated_query)]

        return []

    async def generate_query_with_gpt2(self, user_message):
        # Load GPT-2 model and tokenizer
        model = GPT2LMHeadModel.from_pretrained("gpt2")
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

        # Generate a query using GPT-2
        input_ids = tokenizer.encode(user_message, return_tensors="pt")
        output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

        generated_query = tokenizer.decode(output[0], skip_special_tokens=True)

        return generated_query