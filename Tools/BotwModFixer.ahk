#NoEnv
SendMode Input
SetWorkingDir, %A_ScriptDir%

#If Winactive("content") Or Winactive("aoc")

F5::
    folder := Explorer_GetSelection()

    If InStr(folder, "\") {
        folder := folder . "\..\..\"
    }
    Else {
        folder := folder . "/../"
    }

    Run, "debug.exe", % folder
return

+F5::
    folder := Explorer_GetSelection()

    If InStr(folder, "\") {
        folder := folder . "\..\..\"
    }
    Else {
        folder := folder . "/../"
    }

    Run, %ComSpec% /k "debug.exe", % folder
return

F6::
    folder := Explorer_GetSelection()

    If InStr(folder, "\") {
        folder := folder . "\..\..\"
    }
    Else {
        folder := folder . "/../"
    }

    Run, "pdebug.exe", % folder
return

+F6::
    folder := Explorer_GetSelection()

    If InStr(folder, "\") {
        folder := folder . "\..\..\"
    }
    Else {
        folder := folder . "/../"
    }

    Run, %ComSpec% /k "pdebug.exe", % folder
return

#If

^!F8::
    folder := Explorer_GetSelection()

    If InStr(folder, "\") {
        folder := folder . "\..\..\"
    }
    Else {
        folder := folder . "/../"
    }

    Run, "unfix.exe", % folder
Return

^!+F8::
    folder := Explorer_GetSelection()

    If InStr(folder, "\") {
        folder := folder . "\..\..\"
    }
    Else {
        folder := folder . "/../"
    }

    Run, %ComSpec% /k "unfix.exe", % folder
Return

F8::
    file := Explorer_GetSelection()

    If InStr(file, "\") {
        Run, "shell_sarc.exe" "%file%"
    }

Return

+F8::
    file := Explorer_GetSelection()

    If InStr(file, "\") {
        Run, %ComSpec% /k ""shell_sarc.exe" "%file%""
    }

Return

Explorer_GetSelection(hwnd="") {
    If WinActive("ahk_class CabinetWClass") || WinActive("ahk_class ExploreWClass") || WinActive("ahk_class Progman") {
        WinHWND := WinActive()
        For win in ComObjCreate("Shell.Application").Windows
        If (win.HWND = WinHWND) {
            sel := win.Document.SelectedItems
            for item in sel
                ToReturn .= item.path "`n"
            ToReturnFinal := Trim(ToReturn,"`n")
            if (ToReturnFinal == ""){
                dir := SubStr(win.LocationURL, 9) ; remove "file:///"
                ToReturnFinal := RegExReplace(dir, "%20", " ")
            }
        }
    }
return %ToReturnFinal%
}