def adjust(input, length, padding):
  if length - len(input) == 0:
    return input
  return padding + adjust(input, length - 1, padding)
