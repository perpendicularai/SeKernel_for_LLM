# Plugin class
class Plugin(str):
     pass

# Plugins

# Default plugin
def defaultPlugin():
     system = Plugin(
          """
          You are an intelligent assistant. 
          You always provide well-reasoned answers that are both correct and helpful.
          """
          )
     return system

# Math plugin
def mathPlugin():
     system = Plugin(
          """
          You are an intelligent assistant proficient at Maths. 
          You always provide well-reasoned answers that are both correct and helpful.
          """
          )
     return system
