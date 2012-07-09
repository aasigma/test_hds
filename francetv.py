#!/usr/bin/python

import urllib2
import sys

stream_url = None
#"http://ftvodhdsecz-f.akamaihd.net/z/streaming-adaptatif_france-dom-tom/tdf2012/20120702/etape_0200-,500,900,1600,2250,k.mp4.csmil/manifest.f4m"

vod_key_gen = "http://hdfauth.francetv.fr/esi/urltokengen2.html?url="
live_key_gen = "http://hdfauth.francetv.fr/esi/tokenlive.html?url="

type = "vod"
key_gen = vod_key_gen

def parse_cmd_line(argv):
    global stream_url
    for i in xrange(1, len(argv)):
        arg = argv[i]
        print "arg :", arg
        if arg.startswith("-"):
            if i == len(argv):
                return -1
            if arg == "-t":
                if (len(argv) < i+1) :
                    return -1
        elif stream_url == None :
            stream_url = arg
        else :
            return -1
    return 0

def main(argv):
    global stream_url
    if parse_cmd_line(argv) != 0 :
        print "error parsing command line"
        return -1
    tmp = urllib2.urlopen(vod_key_gen).read()
    url_args = tmp[tmp.find("?")+1:]
    print "url_args :", url_args

    print "open :", stream_url+"?"+url_args
    Manifest = urllib2.urlopen(stream_url+"?"+url_args).read()
    print Manifest

if __name__=="__main__":
    main(sys.argv)
