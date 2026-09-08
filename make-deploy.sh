#!/bin/sh
# Assembles the publishable site into deploy/ — drag that folder into Cloudflare Pages.
# Everything not listed here (brand_assets, tools, _archive, screenshots) stays private.
set -e
cd "$(dirname "$0")"
rm -rf deploy
mkdir -p deploy
cp index.html services.html about.html contact.html reviews.html 404.html deploy/
cp -R assets deploy/
echo "deploy/ ready — $(find deploy -type f | wc -l | tr -d ' ') files, $(du -sh deploy | cut -f1)"
find deploy -type f | sed 's|^deploy/|  |' | sort
