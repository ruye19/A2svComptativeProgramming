class Solution:
    def interpret(self, command: str) -> str:
        for _ in command:
            if "()" in command:
              command = command.replace("()","o")
            else:
               command = command.replace("(al)","al")
        return command       