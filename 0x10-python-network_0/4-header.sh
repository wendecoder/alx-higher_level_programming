#!/bin/bash
# sends GET request with header variable 'X-School-User-Id' and it value 98
curl -sL -H "X-School-User-Id: 98" "$1" -X GET
