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

  # Set messages paraemter equal to data. Depending on your LLM API defintion, messages may be a different parameter, in this case it is messages, as defined in the OpenAI API definition.
  messages = data

  # You may then append any new content and/or messages to the kernel
  data.append(new_message)
  ```

I hope this helps someone starting out. Happy prompting!!!
