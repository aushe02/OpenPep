[Setup]
AppName=OpenPep
AppVersion=0.0.1
WizardStyle=modern
DefaultDirName={autopf}\OpenPep
DefaultGroupName=OpenPep
UninstallDisplayIcon={app}\OpenPep.exe
Compression=lzma2
SolidCompression=yes

[Files]
Source: "../pyinstaller/dist/OpenPep/*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\openMotor"; Filename: "{app}\OpenPep.exe"