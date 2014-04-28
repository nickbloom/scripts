# First install Homebrew

brew install python3
brew install z7za # for Sublimall
brew install markdown




ln -s "/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl

# Python Packages
pip3 insyall ipython3
pip3 install beautifulsoup4
pip3 install collections
pip3 install urllib
pip3 install pandas
pip3 install pelican
pip3 install markdown
pip3 install flake8

# Markdown Custom Processor
-r markdown+simple_tables+table_captions+yaml_metadata_block -w html -S --template=/Users/nbloom/.pandoc/templates/html.template --filter pandoc-citeproc --bibliography=/Users/nbloom/Dropbox/out/globalfiles/bib/complete.bib --mathjax