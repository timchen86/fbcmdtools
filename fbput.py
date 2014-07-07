import facebook
import json
import sys
import os

from os import listdir
from os.path import isfile, join

if len(sys.argv) != 5:
    print "usage: %s oauth_access_token title photo_path n" % sys.argv[0]
    sys.exit(1)

ALBUM_PHOTO_LIMIT=1000

oauth_access_token = sys.argv[1]
title = sys.argv[2]
photo_path = sys.argv[3]
n = int(sys.argv[4])

photos = [ f for f in listdir(photo_path) if isfile(join(photo_path,f)) ]
photos = sorted(photos)

graph = facebook.GraphAPI(oauth_access_token)
if n > ALBUM_PHOTO_LIMIT:
    n = ALBUM_PHOTO_LIMIT

# create album
new_album = graph.put_object("me", "albums", name=title, message="", privacy={"value":"SELF"} )

for p in photos[0:n]:
    path = join(photo_path, p)
    print "uploading: %s" % path 
    time = os.path.splitext(p)[0]
    try:
        graph.put_photo(open(path), time, new_album["id"])
    except KeyboardInterrupt:
        raise
    except:
        pass
