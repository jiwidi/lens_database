#!/usr/bin/env sh

# abort on errors
set -e

# build
npm run build

# navigate into the build output directory
cd dist

echo 'lensdatabase.org' > CNAME

git add -A
git commit -m 'deploy'

git push -f git@github.com:jiwidi/lens_database.git main:gh-pages

cd -