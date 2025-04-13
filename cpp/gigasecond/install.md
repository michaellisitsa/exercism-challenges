## How to install

Follow Getting Started Guide: https://www.boost.org/doc/libs/1_85_0/more/getting_started/unix-variants.html

1. Download boost from link from https://www.boost.org/users/history/version_1_85_0.html and unzip

```bash
curl -LO https://archives.boost.io/release/1.85.0/source/boost_1_85_0.tar.bz2 && tar --bzip2 -xf boost_1_85_0.tar.bz2
```

2. Compile and build the datetime module (necessary for to_string and from_string methods)

```bash
cd dependencies/boost_1_85_0; ./bootstrap.sh --prefix=/Users/michaellisitsa/Documents/lear/cpp/boost/dependencies/boost_1_85_0 --with-libraries=date_time

./b2
```

3. Build

```bash
cd path/to/your/{CmakeLists.txt}
mkdir build
cd build
cmake -G "Unix Makefiles" ..
make
```

4. Run

```bash
./example
```
