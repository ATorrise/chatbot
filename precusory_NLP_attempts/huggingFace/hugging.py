from transformers import GPT2LMHeadModel, GPT2Tokenizer

## File was my space for testing the hugging face transformers. this file changed many times during testing.
## Tests led to my choosing the hugging face SDK

# Load the pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Example: Generate text
input_text = "Once upon a time, "
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)