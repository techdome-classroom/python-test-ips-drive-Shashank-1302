def longest_substring(s: str) -> int:
    
    char_index_map = {}
  left = 0
  max_len = 0

  for right in range(len(s)):
    current_char = s[right]

    # Check if character already exists in the map and is to the right of the current left pointer
    if current_char in char_index_map and char_index_map[current_char] >= left:
      # Update left pointer to be one character after the previous occurrence
      left = max(left, char_index_map[current_char] + 1)

    # Update the character's index in the map
    char_index_map[current_char] = right

    # Update max_len if the current substring is longer
    max_len = max(max_len, right - left + 1)

  return max_len
    pass



