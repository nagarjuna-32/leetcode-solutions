class Solution:

  def removeInvalidParentheses(self, s: str) -> list[str]:
    def is_valid(string: str) -> bool:
      count = 0
      for char in string:
        if char == "(":
          count += 1
        elif char == ")":
          count -= 1
          if count < 0:
            return False
      return count == 0

    # BFS queue and visited set
    queue = {s}
    current_level = {s}
    visited = {s}

    while True:
      # Check if any valid string exists in the current level
      valid_strings = [string for string in queue if is_valid(string)]
      if valid_strings:
        return valid_strings

      # Generate the next level by removing one parenthesis at a time
      next_level = set()
      for string in queue:
        for i in range(len(string)):
          if string[i] in ("(", ")"):
            next_string = string[:i] + string[i + 1 :]
            if next_string not in visited:
              visited.add(next_string)
              next_level.add(next_string)
      queue = next_level