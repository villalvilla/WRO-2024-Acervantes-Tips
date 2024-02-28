# Paso 1: Instalando OpenCV

Lanzamos los siguientes comandos en un terminal:

<pre>
# Update the package list
sudo apt-get update

# Install the dependencies
sudo apt-get install -y build-essential cmake pkg-config libgtk-3-dev \
                        libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
                        libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
                        gfortran openexr libatlas-base-dev python3-dev python-numpy \
                        libtbb2 libtbb-dev libdc1394-22-dev

# Clone the OpenCV repository
git clone https://github.com/opencv/opencv.git

# Clone the OpenCV contrib repository (for additional modules)
git clone https://github.com/opencv/opencv_contrib.git

# Create a build directory
cd opencv
mkdir build
cd build

# Configure the build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D ENABLE_NEON=ON \
      -D ENABLE_VFPV3=ON \
      -D BUILD_TESTS=OFF \
      -D OPENCV_ENABLE_NONFREE=ON \
      -D INSTALL_PYTHON_EXAMPLES=OFF \
      -D OPENCV_PYTHON3_INSTALL_PATH=/usr/local/lib/python3.5/dist-packages \
      -D BUILD_EXAMPLES=OFF ..

# Compile OpenCV
make -j4

# Install OpenCV
sudo make install

# Remove the build directory
cd ..
rm -rf build
</pre>
