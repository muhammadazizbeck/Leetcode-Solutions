class Solution:
    def interpret(self, command: str) -> str:
        while "()" in command or "(al)" in command:
            if "()" in command:
                command = command.replace("()","o")
            if "(al)" in command:
                command = command.replace("(al)","al")

        return command