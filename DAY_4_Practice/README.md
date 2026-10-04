# AI Fluency Course – Day 1 Lab

## Aim

To set up a Python development environment in VS Code, connect it to an open large language model, and compare three systems on the same task:

1. Chatbot
2. Rule-Based Workflow
3. AI Agent

## Files Included

- config.py
- check_setup.py
- chatbot.py
- workflow.py
- tools.py
- agent.py
- challenge.py
- check_key.py
- test_groq.py
- requirements.txt

## Environment

- Python
- Provider: Groq
- Model: openai/gpt-oss-20b
- Editor: VS Code

## Output 1 – Setup Verification

Python version : 3.x.x
Provider       : groq
Model          : openai/gpt-oss-20b
Calling the model ...
Model replied  : SETUP OK

Setup check finished.

## Output 2 – Rule-Based Workflow

=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===

Q: What is the fee for AI202?
A: Fee for AI202: Rs. 18,000

Q: What is the total fee for CS101 and AI202 after a 10% scholarship?
A: Total fee: Rs. 27,000

Q: Is DS303 more expensive than CS101, and by how much?
A: Sorry, I do not have a rule for this type of question.

Q: Write a two-line welcome message for new AI students.
A: Sorry, I can only answer questions about course fees.

## Output 3 – Tool Testing

get_course_fee('ai202') -> 18000

calculator('(12000 + 18000) * 0.9') -> 27000.0

calculator('15000 - 12000') -> 3000

## Output 4 – AI Agent

=== SYSTEM 3: AI AGENT | provider: groq | model: openai/gpt-oss-20b ===

Q: What is the fee for AI202?

step 1: get_course_fee({'course_code': 'AI202'}) -> 18000

A: The fee for AI202 is ₹18,000.

The AI Agent uses the LLM and available tools to answer the question.

## Output 5 – Challenge Question

Question:

I can pay Rs. 30,000.
Which two courses can I take together within this budget?

Workflow Output:

Sorry, I can only answer questions about course fees.

Agent Output:

You can take either of the following pairs of courses within your Rs. 30,000 budget:

CS101 + AI202 = Rs. 30,000
CS101 + DS303 = Rs. 27,000

Both combinations stay within your Rs. 30,000 budget.

## Observations

| System | Strength | Limitation |
|---|---|---|
| Chatbot | Natural language responses | Does not know private fee data |
| Rule-Based Workflow | Reliable and predictable | Cannot answer new question types |
| AI Agent | Can use tools and solve complex queries | Depends on model's tool-calling capability |

## Conclusion

The chatbot is flexible and can generate natural language responses, but it does not have access to private course-fee data.

The rule-based workflow is reliable and predictable for predefined questions, but it cannot handle new question types.

The AI agent combines an LLM with tools and can use available information and calculations to handle more complex tasks.

This lab demonstrates the basic difference between a Chatbot, Rule-Based Workflow, and AI Agent.

## Key Concept

Chatbot = LLM

Rule-Based Workflow = Rules + Data

AI Agent = LLM + Tools + Loop

