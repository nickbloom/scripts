cd ~
mkdir R
cd R
wget http://rweb.quant.ku.edu/cran/src/base/R-3/R-3.1.0.tar.gz
tar -xf R-3.1.0.tar.gz
cd R-3.1.0
./configure --prefix=$HOME && make && make install


# NOTE: After you're done, you'll want to do a couple of things:
# 1. create a directory for packages:
# cd ~ && mkdir R/packages
# 2. Add this to your .Rprofile without quotes (if you don't know how to use vim, you can do this from within the Paradigm version of RStudio): '.libPaths( "~/R/packages" )'
# 3. add your $HOME/bin to your path in .profile for .bashrc: 'export PATH=$HOME/bin:$PATH' (without quotes)
# 4. Reload your .profile file: 'source ~/.profile'