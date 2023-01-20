import tkinter as tk
import string
import secrets

# All possible symbols
digits = string.digits
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
punc = string.punctuation


# Event Handlers
# Generate Password
def genPassword():
    # Call symbol function to see which symbol lists to use
    defaultSyms = lowercase + digits
    # Call length function to get length to use
    defaultLen = 16
    # Using requested symbols & length, generate password
    secretsGen = secrets.SystemRandom()
    randomPwd = secretsGen.sample(defaultSyms, defaultLen) 
    # Send generated password to display function
    displayPwd(randomPwd)

# Display Password
def displayPwd(pwd):
    pwdLabel['text'] = pwd
# Copy Password
# Get Password Length
# Confirm included symbols 
#def includedSymbols():
    # Check what symbols are marked
    # Create super list based on what symbols are checked
    # Pass super list to genPassword


# New Window
window = tk.Tk()
window.title('Password Generator')
window.resizable(False, False)

# Frame: Base frame to hold all other frames
baseFrame = tk.Frame(master=window,
                     height=300,
                     width=500,
                     bg='dark grey')
baseFrame.pack(fill=tk.BOTH)


# Frame: Generate Password
generatorFrame = tk.Frame(master=baseFrame,
                          height=100,
                          width=500)
generatorFrame.pack(fill=tk.X)

# Button: Copy Password
copyBtn = tk.Button(master=generatorFrame, text='Copy')
copyBtn.pack(side=tk.LEFT)

# Label: Display Password
pwdLabel = tk.Label(master=generatorFrame,
                    width=20,
                    text='.............................',
                    bg='dark grey')
pwdLabel.pack(side=tk.LEFT)

# Button: Generate New Password
refreshPwd = tk.Button(master=generatorFrame, text="Refresh", command=genPassword)
refreshPwd.pack(side=tk.LEFT)


# Frame: Header for Length of Password
lengthHdrFrame = tk.Frame(master=baseFrame, height=50, width=500)
lengthHdrFrame.pack(fill=tk.X)

# Label: Widget Header
lengthHdrLabel = tk.Label(master=lengthHdrFrame, text='\nLength:')
lengthHdrLabel.pack(side=tk.LEFT)


# Frame: Length of Password
lengthFrame = tk.Frame(master=baseFrame, height=100, width=500)
lengthFrame.pack(fill=tk.X)

# Slider: Adjust length of Generated Password
lengthSlider = tk.Scale(master=lengthFrame, from_=0, to=50, orient='horizontal', showvalue=False)
lengthSlider.pack(side=tk.LEFT)

# Entry: Hold Current Value of the Slider, and manually input length value
manLengthEntry = tk.Entry(master=lengthFrame, width=4)
manLengthEntry.pack(side=tk.LEFT)


# Frame: Symbols Header
symbolsHdrFrame = tk.Frame(master=baseFrame, height=50, width=500)
symbolsHdrFrame.pack(fill=tk.X)

# Label: Symbols header label
symbolsHdrLabel = tk.Label(master=symbolsHdrFrame, text="\nSymbols:")
symbolsHdrLabel.pack(side=tk.LEFT)


# Frame: Symbols Included in Password
symbolsFrame = tk.Frame(master=baseFrame, height=100, width=500)
symbolsFrame.pack(fill=tk.X)


# Checked variables
cDigits = tk.StringVar()
cDigits.set(digits)
cUpper = tk.StringVar()
cUpper.set(uppercase)
cLower = tk.StringVar()
cLower.set(lowercase)
cPunc = tk.StringVar()
cPunc.set(punc)

# Checkboxes: Symbols to be Included in Password: Digits, Punctuation, Uppercase, Lowercawse
#Digits
digitsCBox = tk.Checkbutton(master=symbolsFrame, text="Digits", variable=cDigits)
digitsCBox.pack(side=tk.LEFT)
#Punctuation
puncCBox = tk.Checkbutton(master=symbolsFrame, text="Punctuation", onvalue=1, offvalue=0)
puncCBox.pack(side=tk.LEFT)
#Uppercase
upperCBox = tk.Checkbutton(master=symbolsFrame, text="Uppercase", onvalue=1, offvalue=0)
upperCBox.pack(side=tk.LEFT)
#Lowercase
lowerCBox = tk.Checkbutton(master=symbolsFrame, text="Lowercase", onvalue=1, offvalue=0)
lowerCBox.pack(side=tk.LEFT)


# Execute Mainloop
window.mainloop()