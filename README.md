# 🃏 SeKernel_for_LLM
This is a Python module used to create a semantic kernel in your openai api compatible chat applications.

### 🍬 Features
- In-chat memory
- Internet-search
- Database querying

## ⚙️ How to:
- Clone the repo and import the modules into your project. Ensure that it is in the project directory.
- ```
  import kernel
  import plugins

  ### DATABASE ###
  - Using this database plugin
  -- Initialize the database plugin
  db = plugins.dbConn()

  - Use the database plugin along with the dbChatPlugin
  data = kernel.chatTemplate(prompt=prompt, plugin=plugins.dbChatPlugin())

  - Excuting the query
  db.execute(response)

  - Getting the output
  response = db.fetchall()

  ### INTERNET-SEARCH ###
  - Define search plugin
  search_prompt = plugins.searchPlugin(output=question) # If context equals None, use the Chat template. See `kernel.py` for more templates.

  - Initialize the kernel
  data = kernel.shopTemplate(prompt=prompt, plugin=plugins.defaultPlugin(), context=search_prompt or context=None # Where no context is provided, and so you may assume the AI assistant to not have any awareness of information of events that took place after the date until which it's training data is up until) # See plugins.py module for more plugins

  LlamaCpp
  client = Llama(
        model_path=kernel.model() # Make sure to add your GGUF model in the kernel module.
  )

  - Use the kernel and set messages parameter equal to data. Depending on your LLM API defintion, messages may be a different parameter, in this case it is messages, as defined in the OpenAI API definition.
  output = client.create_chat_completions(
    messages = data
  )
  ```
  See [OpenAI](https://platform.openai.com/docs/api-reference/chat/create) API reference for more.
- ```
  - You may then append any new content and/or messages to the kernel
  data.append(new_message)
  ```
## 📽️ Short Films
See examples of using the SeKernel_for_LLM with 🦙 [LlamaCpp Python bindings](https://github.com/abetlen/llama-cpp-python)

#### The square-root of 2
https://github.com/user-attachments/assets/cb48e962-2cba-4672-b4e7-c0f77455bb74

#### Internet search with Google for the price of leggings
https://github.com/user-attachments/assets/fdf5ac16-c8b7-4b39-b91b-d4e2d8d2d888

#### Database query
https://github.com/user-attachments/assets/ad9c87a4-475f-4ca0-a576-109709ca84b0






I hope this helps someone starting out. :octocat: Happy prompting!!!
