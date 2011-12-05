%global fontname saab
%global fontconf 67-%{fontname}.conf

Name:        %{fontname}-fonts
Version:     0.91
Release:     4%{?dist}
Summary:     Free Punjabi Unicode OpenType Font

Group:       User Interface/X
License:     GPLv3+ with exceptions
URL:         http://guca.sourceforge.net/typography/fonts/saab/
Source0:     http://downloads.sf.net/guca/saab.0.91.zip
Source1:   %{name}-fontconfig.conf
BuildArch:   noarch
BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: fontpackages-devel
Requires:    fontpackages-filesystem

%description 
This package provides a free OpenType Punjabi (Gurmukhi) font. 
Developed by Bhupinder Singh


%prep
%setup -q -c

%build
echo "Nothing to do in Build."

%install
rm -rf $RPM_BUILD_ROOT
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p Saab.otf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -rf $RPM_BUILD_ROOT

%_font_pkg Saab.otf -f %{fontconf}
%doc

%changelog
* Mon Feb 08 2010 Parag <pnemade AT redhat.com> - 0.91-4
- Resolves: rh#560877 - please update the license of saab-fonts

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.91-3.1
- Rebuilt for RHEL 6

* Tue Sep 04 2009 A S Alam <aalam@redhat.com> - 0.91-3
- Add fontconfig conf file

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 2 2009 A S Alam <aalam@redhat.com> - 0.91-1
- New Package Build for Punjabi Unicode Font
