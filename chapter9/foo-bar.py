def foo():
  def bar(i):
    if i > 0:
      return i + bar(i - 1)
    else:
      return 0
  
  return f"Result is: {bar(10)}"

print(foo())