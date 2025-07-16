#!/bin/bash
cd /Users/dmitrypyanov/dmitry-website
git add index.html style.css
git commit -m "Update website: remove music festival section, add Mindpet section, update to courier font design"
git push
echo "Deployment complete!"