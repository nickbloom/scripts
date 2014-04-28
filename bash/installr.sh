cd ~
mkdir R
cd R
wget http://rweb.quant.ku.edu/cran/src/base/R-3/R-3.1.0.tar.gz
tar -xf R-3.1.0.tar.gz
cd R-3.1.0
./configure --prefix=$HOME && make
