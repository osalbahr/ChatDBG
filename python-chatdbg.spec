Name:           python-chatdbg
Version:        1.0.0
Release:        %autorelease
Summary:        AI-assisted debugging. Uses AI to answer 'why'.

License:        Apache-2.0
URL:            https://github.com/plasma-umass/ChatDBG
Source:         %{pypi_source chatdbg}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This is package 'chatdbg' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-chatdbg
Summary:        %{summary}

%description -n python3-chatdbg %_description


%prep
%autosetup -p1 -n chatdbg-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files -l ...


%check
%pyproject_check_import


%files -n python3-chatdbg -f %{pyproject_files}


%changelog
%autochangelog
