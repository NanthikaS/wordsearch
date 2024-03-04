# import tkinter as tk
# from tkinter import filedialog
# import webbrowser

# def open_document():
#     document_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
#     if document_path:
#         with open(document_path, 'r') as file:
#             document_text.delete(1.0, tk.END)
#             document_text.insert(tk.END, file.read())

# def search_word(event):
#     # Get the selected word or sentence from the text widget
#     selected_text = document_text.selection_get()

#     # Construct a search query URL using the selected text
#     search_query = "https://www.google.com/search?q=" + selected_text
#     # 
#     # Open the search query in a web browser
#     webbrowser.open_new_tab(search_query)

# # Create the main window
# root = tk.Tk()
# root.title("Document Viewer")

# # Create a text widget to display the document
# document_text = tk.Text(root, wrap="word", height=20, width=80)
# document_text.pack(fill="both", expand=True)

# # Create a menu bar
# menu_bar = tk.Menu(root)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open Document", command=open_document)
# menu_bar.add_cascade(label="File", menu=file_menu)
# root.config(menu=menu_bar)

# # Bind the mouse click event to search for the selected word
# document_text.bind("<ButtonRelease-1>", search_word)

# # Start the GUI event loop
# root.mainloop()


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
    # app.run(debug=True)
from flask import Flask, render_template, request
import webbrowser
import pyperclip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/open_document', methods=['POST'])
def open_document():
    file = request.files['document']
    if file:
        document_content = file.read().decode('utf-8')
        return document_content
    else:
        return "No document selected"

@app.route('/search_word', methods=['POST'])
def search_word():
    selected_word = request.form['selected_word']
    if selected_word:
        search_query = "https://www.google.com/search?q=" + selected_word
        webbrowser.open_new_tab(search_query)
        return "Searching for: " + selected_word
    else:
        return "No word selected"

if __name__ == '__main__':
    app.run(debug=True)
