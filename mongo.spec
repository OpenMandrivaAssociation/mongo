%define name    mongo
%define version 2004.08.17
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	Filesystem load tester
URL:		http://thebsh.namesys.com/benchmarks/dist
License:	GPL
Group:		System/Kernel and hardware
Source0:	%{name}-%{version}.tar.gz

%description
Mongo is a program to test linux filesystems for performance and
functionality.
The way to run a Mongo test is runing the mongo.pl script. The mongo.pl
creates output files can be parsed by mongo_parse.pl script.

%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%_bindir
install -m 755 mongo_append mongo_copy $RPM_BUILD_ROOT%_bindir
install -m 755 mongo_delete mongo_parser.pl $RPM_BUILD_ROOT%_bindir
install -m 755 summ map5 mongo_modify $RPM_BUILD_ROOT%_bindir
install -m 755 mongo.pl mongo_slinks $RPM_BUILD_ROOT%_bindir
install -m 755 reiser_fract_tree mongo_dd mongo_holes $RPM_BUILD_ROOT%_bindir
install -m 755 mongo_read update-flist.pl $RPM_BUILD_ROOT%_bindir

install -d $RPM_BUILD_ROOT%_defaultdocdir/%name-%version
cp README $RPM_BUILD_ROOT%_defaultdocdir/%name-%version
cp mongo.cmds.example $RPM_BUILD_ROOT%_defaultdocdir/%name-%version

%files
%attr(755,root,root)
%_bindir/mongo_append
%_bindir/mongo_copy
%_bindir/mongo_delete
%_bindir/mongo_parser.pl
%_bindir/summ
%_bindir/map5
%_bindir/mongo_modify
%_bindir/mongo.pl
%_bindir/mongo_slinks
%_bindir/reiser_fract_tree
%_bindir/mongo_dd
%_bindir/mongo_holes
%_bindir/mongo_read
%_bindir/update-flist.pl
%_defaultdocdir/%name-%version

%clean
rm -rf $RPM_BUILD_ROOT


