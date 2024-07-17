# SeKernel_for_LLM
This is a Python module used to create memory in your chat applications.

## ⚙️ How to:
- Clone the repo and import the module into your project. Ensure that it is in the project directory.
- ```
  import kernel

  # Initialize the kernel
  data = kernel

  # Create a template
  data = [
    {"role": "system", "content": """You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."""},
    {"role": "user", "content": question},
  ]

  # Set messages parameter equal to data. Depending on your LLM API defintion, messages may be a different parameter, in this case it is messages, as defined in the OpenAI API definition.
  messages = data
  ```
  See [OpenAI](https://platform.openai.com/docs/api-reference/chat/create) for more.
  
  ```
  # You may then append any new content and/or messages to the kernel
  data.append(new_message)
  ```
## 📽️ Short Films
See an example of using the SeKernel_for_LLM with 🦙 [LlamaCpp Python bindings](https://github.com/abetlen/llama-cpp-python)

https://github.com/user-attachments/assets/cb48e962-2cba-4672-b4e7-c0f77455bb74


🍾 I hope this helps someone starting out. Happy prompting!!!
