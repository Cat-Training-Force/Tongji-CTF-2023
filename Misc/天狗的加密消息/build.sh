#!/bin/bash

mkdir -p build

SOURCEFILE_PREFIX="tougue_dog"
SOURCEFILE_SUFFIX=".py"
SOURCEFILE=$SOURCEFILE_PREFIX$SOURCEFILE_SUFFIX

cp $SOURCEFILE ./build

for minor in {3..11};
do
    docker_image_tag="python:3.$minor-alpine"
    echo "Building for Python 3."$minor, pulling from $docker_image_tag...
    echo
    docker pull $docker_image_tag
    docker run -v $(pwd)/build:/build -u $(id -u):$(id -g) $docker_image_tag sh -c 'cd /build && python -m py_compile '$SOURCEFILE
    echo
    echo "Building for Python 3."$minor completes.
    echo
done

cd build/__pycache__
for f in *.pyc; do mv "$f" $(basename $f .pyc).jpg; done
echo "Renamed pyc to jpg."

cd ..
mv __pycache__ $SOURCEFILE_PREFIX
rm $SOURCEFILE
echo "Renamed __pycache__ to $SOURCEFILE_PREFIX. Build completes."