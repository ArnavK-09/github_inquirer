#!/bin/bash

# Navigate to the 'agent' directory and run the Poetry agent in the background
cd agent || exit
poetry run agent &

# Return to the root directory
cd ..

# Navigate to the 'ui' directory and start the development server
cd gui || exit
npm run dev
