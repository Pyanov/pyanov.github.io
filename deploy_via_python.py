#!/usr/bin/env python3
import subprocess
import os

# Change to the website directory
os.chdir('/Users/dmitrypyanov/dmitry-website')

try:
    # Git add
    print("Adding files...")
    result = subprocess.run(['git', 'add', 'index.html', 'style.css'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error adding files: {result.stderr}")
    else:
        print("Files added successfully")
    
    # Git commit
    print("\nCommitting changes...")
    commit_message = "Update website: remove music festival section, add Mindpet section, update to courier font design"
    result = subprocess.run(['git', 'commit', '-m', commit_message], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error committing: {result.stderr}")
    else:
        print("Changes committed successfully")
        print(result.stdout)
    
    # Git push
    print("\nPushing to GitHub...")
    result = subprocess.run(['git', 'push'], 
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error pushing: {result.stderr}")
    else:
        print("Successfully pushed to GitHub!")
        print(result.stdout)
        
except Exception as e:
    print(f"An error occurred: {e}")

print("\nDeployment script complete.")