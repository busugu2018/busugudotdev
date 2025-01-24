import os

# Path to your images folder
folder_path = "/Volumes/Nzieng SSD1/Nzieng SSD1/IT/Portfolio/Portfolio website/busugudotdev/awsP3"
output_file = "awsP3.html"

# Open a file to save the HTML
with open(output_file, "w") as file:
    file.write("<div id='image-container'>\n")
    
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")):
            file.write(f"<img src='awsP3/{awsp3step1.png}' alt='{awsp3step1.png}' loading='lazy'>\n")
    
    file.write("</div>")

print(f"HTML file with <img> tags saved as {output_file}")