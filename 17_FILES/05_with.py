with open ("17_FILES/rayan.txt","r") as f:
    content = f.read()
    print(content)
    # No need o write f.close() cz file is already closed by default when using with syntax