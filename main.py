# from client import call_llm
from memory import messages
from client import call_llm
from tool import search   # you will create this

while True:
    query = input('user: ')
    if query == 'exit':
        break

    messages.append({"role": "user", "content": query})

    for step in range(5):  # prevent infinite loops
        response = call_llm(messages)
        content = response["content"]

        print("LLM:", content)

        # CASE 1: Final Answer
        if "Final Answer:" in content:
            final = content.split("Final Answer:")[1].strip()
            print("AI:", final)

            messages.append({"role": "assistant", "content": content})
            break

        # CASE 2: Tool Call
        elif "Action:" in content:
            try:
                lines = content.split("\n")
                action = None
                tool_input = None

                for line in lines:
                    if line.startswith("Action:"):
                        action = line.split("Action:")[1].strip()
                    elif line.startswith("Input:"):
                        tool_input = line.split("Input:")[1].strip()

                if action == "search":
                    result = search(tool_input)
                else:
                    result = "Unknown tool"

                print("TOOL INPUT:", tool_input)
                print("TOOL RESULT:", result)

                # memory
                messages.append({"role": "assistant", "content": content})
                messages.append({
                    "role": "assistant",
                    "content": f"Observation: {result}"
                })

            except Exception as e:
                print("Parsing error:", e)
                break

        else:
            print("Unexpected format:", content)
            break

# while True:
#     query = input('user: ')
#     if query == 'exit':
#         break
#     messages.append({"role": "user", "content": query})
#     response = call_llm(messages)
#     messages.append({"role": "assistant", "content": response})
#     print('AI: ', response)