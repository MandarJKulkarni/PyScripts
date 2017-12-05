# Add this script to a folder where your python scripts are present
# Or add the folder containing this script to PYTHONPATH environment variable value
import sys
import webbrowser
if sys.argv[1] is not None:
    url ="https://www.google.co.in/search?q="+sys.argv[1]
    webbrowser.open(url)
