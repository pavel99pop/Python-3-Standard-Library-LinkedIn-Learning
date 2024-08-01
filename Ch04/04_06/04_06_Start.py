# Text Wrap Module
import textwrap

websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent:")
print(textwrap.fill(websiteText))
print()

print("Dedent")
print(textwrap.dedent(websiteText).strip())
print()

print("Fill")
print(textwrap.fill(websiteText, width=50))
print()

print("Controlling Indent")
print(textwrap.fill(websiteText, initial_indent='', subsequent_indent='   '))
print()

print("Shortening Text")
print(textwrap.shorten(websiteText, width=15, placeholder='...'))
print()