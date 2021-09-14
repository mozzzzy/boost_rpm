# boost_rpm
Config files to build rpm packages of boost.

## Download package from Github Release
### RPM package
```bash
$ curl -s https://api.github.com/repos/mozzzzy/boost_rpm/releases | \
  jq '.[].assets[] | select(.name == "self-built-boost-1.76.0-0.el7.x86_64.rpm")' | \
  jq '.url' | \
  xargs curl -vLJO -H 'Accept: application/octet-stream'
```

## Build
### Build rpm packages
```bash
$ make all
```
Then the rpm packages are created in `rpmbuild/RPMS/x86_64` and `rpmbuild/SRPMS`.
```bash
$ tree rpmbuild/ -I BUILD
rpmbuild/
|-- BUILDROOT
|-- RPMS
|   `-- x86_64
|       |-- self-built-boost-1.76.0-0.el7.x86_64.rpm
|       `-- self-built-boost-debuginfo-1.76.0-0.el7.x86_64.rpm
|-- SOURCES
|   `-- boost_1_76_0.tar.gz
|-- SPECS
|   `-- self-built-boost.spec
`-- SRPMS
    `-- self-built-boost-1.76.0-0.el7.src.rpm

6 directories, 5 files
```
