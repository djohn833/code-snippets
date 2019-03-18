#!/bin/bash

# Find files that have LF line endings, instead of CRLF.
find "$1" -print0 |\
    xargs -0 file |\
    grep -w LF |\
    awk -F: '{ print $1 }'
