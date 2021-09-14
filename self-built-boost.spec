Name:    self-built-boost
Version: 1.76.0
Release: 0%{?dist}
Summary: The free peer-reviewed portable C++ source libraries
License: Boost and MIT and Python
URL:     http://www.boost.org
Source0: boost_1_76_0.tar.gz

BuildRequires:  python-devel

# Avoid "No build ID note found" error
%undefine _missing_build_ids_terminate_build

%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been included in the C++ 2011 standard and
others have been proposed to the C++ Standards Committee for inclusion
in future standards.)

%prep
%setup -n boost_1_76_0


%build
./bootstrap.sh
./b2 -j2


%install
./b2 install --prefix=%{buildroot}/opt
for name in \
  atomic \
  chrono \
  container \
  context \
  contract \
  coroutine \
  date_time \
  exception \
  fiber \
  fiber_numa \
  filesystem \
  graph \
  graph_parallel \
  headers \
  iostreams \
  json \
  locale \
  log \
  log_setup \
  math_c99 \
  math_c99f \
  math_c99l \
  math_tr1 \
  math_tr1f \
  math_tr1l \
  mpi \
  nowide \
  prg_exec_monitor \
  program_options \
  python \
  random \
  regex \
  serialization \
  stacktrace_addr2line \
  stacktrace_backtrace \
  stacktrace_basic \
  stacktrace_noop \
  stacktrace_windbg \
  stacktrace_windbg_cached \
  system \
  test_exec_monitor \
  thread \
  timer \
  type_erasure \
  unit_test_framework \
  wave \
  wserialization \
; do
  sed -i -e 's/\/.*%{_arch}//g' \
    %{buildroot}/opt/lib/cmake/boost_${name}-%{version}/boost_${name}-config.cmake
done


%files
/opt/lib/*
/opt/include/*


%changelog
