@set MYTOOLS=c:\my\tools

@path=%path%;%MYTOOLS%\bin
@path=%path%;%MYTOOLS%\bat
@path=%path%;%MYTOOLS%\vslick\win
@path=%path%;c:\my\tools\Vim\vim81
@path=%path%;c:\my\tools\vslick\win

@alias -f %MYTOOLS%\bat\python.ali

@cd /d c:\Workspace\PyCode
