# Added some "Module" And "Pip"

# Import the pyjokes module
import pyjokes

# Print a single random joke
print("😂 Here’s a random programming joke for you:")
print(pyjokes.get_joke())

# Optional: multiple jokes loop
print("\n🤖 More Jokes for Fun:\n")
for i in range(3):
    joke = pyjokes.get_joke(language="en", category="neutral")
    print(f"{i+1}. {joke}\n")
