name = "Gera"
greeting = "Hello, {}"   # this would be like a template
with_name = greeting.format(name)  # here is where we give the variable name, a value

print(with_name)


longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Gera", "Monday")

print(formatted)

