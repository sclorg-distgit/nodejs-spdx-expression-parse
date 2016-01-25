%{?scl:%scl_package nodejs-spdx-expression-parse}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-spdx-expression-parse

%global npm_name spdx-expression-parse
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-spdx-expression-parse
Version:	1.0.1
Release:	1%{?dist}
Summary:	parse SPDX license expressions
Url:		https://github.com/kemitchell/spdx-expression-parse.js#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	(MIT AND CC-BY-3.0)

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

%doc README.md

%changelog
* Mon Nov 23 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build
