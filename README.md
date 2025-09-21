# isntaUnfollowTrackingPython
Simple python 3 script which uses exported following/followers data to list people who don't follow you back

You need Python 3 installes and BeautifulSoup if you don’t have it:
pip install beautifulsoup4

1. Export your data:
https://accountscenter.instagram.com/info_and_permissions/
You can just choose 'Followers & Following', the rest of the data is not needed.

2. Put the following files in the same folder as the python script
following.html
followers_1.html

3. (Optional) - whitelist nicknames you don't want to include in the final result by adding them to 
exclusions.txt
in the format as below (line by line):
profile1
profile2
...

4. Run the script
not_following_back_html_txt.py

5. Two files will be created
not_following_back.html - clickable links to profiles of people who don't follow you back
not_following_back.txt - a list of nicknames (line by line) of people who don't follow you back (the same as above, but not clickable, can be used to create a whilelist)

6. Unfollow ungrateful people who don't follow you back :)
