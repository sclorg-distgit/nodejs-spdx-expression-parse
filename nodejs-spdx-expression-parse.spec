%{?scl:%scl_package nodejs-spdx-expression-parse}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-spdx-expression-parse

%global npm_name spdx-expression-parse
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-spdx-expression-parse
Version:	1.0.2
Release:	2%{?dist}
Summary:	Parse SPDX license expressions
Url:		https://github.com/kemitchell/spdx-expression-parse.js#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# CC license that is missing from sources
# http://creativecommons.org/licenses/by/3.0/
Source1:    LICENSE-CC-BY-3.0
License:	MIT AND CC-BY-3.0

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(defence-cli)
BuildRequires:	%{?scl_prefix}npm(jison)
BuildRequires:	%{?scl_prefix}npm(replace-require-self)
BuildRequires:	%{?scl_prefix}npm(uglify-js)
%endif

BuildRequires:	%{?scl_prefix}npm(spdx-exceptions)
BuildRequires:	%{?scl_prefix}npm(spdx-license-ids)

Requires:	%{?scl_prefix}npm(spdx-exceptions)
Requires:	%{?scl_prefix}npm(spdx-license-ids)

%description
parse SPDX license expressions

%prep
%setup -q -n package
cp -p %{SOURCE1} .

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/spdx-expression-parse

%doc README.md LICENSE LICENSE-CC-BY-3.0

%changelog
* Fri Jun 10 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-2
- Resolves: #1334856 , update, add missing license

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-2
- rebuilt

* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build
