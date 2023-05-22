import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key = <INSERT-YOUR-OPENAI-API-KEY-HERE>
#get your key from the link below
#https://platform.openai.com/account/api-keys

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

prompt = f"""
Determine if the student response to each question is correct or not
Give the answer in json format with the following properties:
The question number
The question
The students response
Explain the right solution to the question. start with the phrase “your response...”
The grade of the student for each question, the grade should be over 100.
be very lenient with your grading and try to solve the question yourself before grading
```
1)
Question: What is C++ Programming Language

Question Guide Answer: C++ is an object-oriented programming language which gives a clear structure to programs and allows code to be reused, lowering development costs.

Student's response: 
C++ is a general-purpose, object-oriented programming language. It was created by Bjarne Stroustrup at Bell Labs circa 1980. C++ is very similar to C (invented by Dennis Ritchie in the early 1970s). C++ is so compatible with C that it will probably compile over 99% of C programs without changing a line of source code. Though C++ is a lot of well-structured and safer language than C as it OOPs based.

2)
Question: What is political apathy

Question Guide Answer: political apathy is a lack of interest or apathy towards politics


Student's response: Politcal apathy is when someone don’t like politics


3)
Question: Why can no object move faster than the speed of light in vacuum

Question Guide Answer: As an object goes faster and faster, its mass increases. If the mass of objects become infinite as they get closer to the speed of light, it makes sense that you cannot break that speed barrier — it would take infinite energy to accomplish.


Student's response: it is because the mass of objects becoming infinitely large as it approaches the speed of light
```

Also calculate the grade avarage after going through each question

"""
response = get_completion(prompt)
print(response)
