Name:           opencloud-desktop-shell-integration-resources
Version:        1.0.0
Release:        %{autorelease}
Summary:        Icons for OpenCloud linux desktop plugins

License:        GPL-2.0-only
URL:            https://github.com/opencloud-eu/desktop-shell-integration-resources
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/pull/6.patch

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
Requires:       hicolor-icon-theme

%description
Icons for OpenCloud linux desktop plugins.

%prep
%autosetup -n desktop-shell-integration-resources-%{version}
%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license COPYING
%doc README.md
%{_datadir}/icons/hicolor/*/apps/OpenCloud_*.png
%dir %{_datadir}/cmake/OpenCloudShellResources
%{_datadir}/cmake/OpenCloudShellResources/OpenCloudShellResourcesConfig.cmake
%{_datadir}/cmake/OpenCloudShellResources/OpenCloudShellResourcesConfigVersion.cmake

%changelog
%autochangelog
