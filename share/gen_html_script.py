import os

# Directory containing images
image_directory = 'dk721'
output_html = 'index.html'

# List of image file extensions
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

# Create HTML content
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Display All Images</title>
</head>
<body>

    <h1>Total average image</h1>
    <!-- Path goes up one level, then into 'result/241105_dynamic_test' to access 'Total.png' -->
    <img src="Total.png" alt="Total Image" style="max-width:100%; height:auto;">
    <br><br>
    
    <h1>All Images in /dk721/</h1>
    <div style="display: flex; flex-wrap: wrap;">
"""

# Loop through all files in the directory
for filename in os.listdir(image_directory):
    if filename.lower().endswith(image_extensions):
        # Add each image to the HTML content
        html_content += f'        <div style="margin: 10px;"><img src="{image_directory}/{filename}" alt="{filename}" style="max-width:400px; height:auto;"></div>\n'

# Close the HTML tags
html_content += """    </div>
</body>
</html>
"""

# Write the HTML content to a file
with open(output_html, 'w') as file:
    file.write(html_content)

print(f"HTML file '{output_html}' generated successfully.")
