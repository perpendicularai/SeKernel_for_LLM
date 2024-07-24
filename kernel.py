# List class
class MyList(list):
     pass

# Model class
class Model(str):
     pass

# Template function that takes a string as input and returns a list
def template(prompt:str, plugin):
     my_list = MyList
     my_list = [
          {"role": "system", "content": plugin},
          {"role": "user", "content": prompt},
          ]
     return my_list

# Model function that returns the model as a string
def model():
     model = Model("<PATH TO GGUF MODEL>")
     return model