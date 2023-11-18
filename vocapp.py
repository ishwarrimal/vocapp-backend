import cohere
from dotenv import load_dotenv
import os

load_dotenv() # This line brings all environment variables from .env into os.environ

cohere_api_key = os.environ['COHERE_API_KEY']

co = cohere.Client(cohere_api_key)

def generate_text(user_prompt):
  response = co.generate(
    model='command-xlarge-nightly',
    prompt=user_prompt,
    # Degree of randomness, less temprature means more specific answer
    temperature=0, 
    # k ensures only top k tokens are used for generating the resonse
    k=0,
    p=0.75,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=[],
    return_likelihoods='NONE'
  )
  return response.generations[0].text

cohere_api_output = generate_text("Can any word from the given word list be used in the sentence 'I think I like that girl' with any word from [furious, contagious, admire], if yes please rewrite else say NO. I don't need anything other than the replaced sentence as answer")

print(cohere_api_output)