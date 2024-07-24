# Plugin class
class Plugin(str):
     pass

# Plugins
def defaultPlugin():
     system = Plugin(
          """
          You are an intelligent assistant. 
          You always provide well-reasoned answers that are both correct and helpful.
          """
          )
     return system

def mathPlugin():
     system = Plugin(
          """
          You are an intelligent assistant proficient at Maths. 
          You always provide well-reasoned answers that are both correct and helpful.
          """
          )
     return system