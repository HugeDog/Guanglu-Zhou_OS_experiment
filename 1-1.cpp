// proccreate项目
#include <windows.h>
#include <iostream>
#include <stdio.h>

// 
void StartClone(int nCloneID)
{
    // 
    TCHAR szFilename[MAX_PATH] ;
    :: GetModuleFileName(NULL, szFilename, MAX_PATH) ;

    // 
    TCHAR szCmdLine[MAX_PATH];
	:: sprintf(szCmdLine,"\"%s\" %d",szFilename,nCloneID);

	// 
    STARTUPINFO si;
    :: ZeroMemory(reinterpret_cast <void*> (&si) , sizeof(si) ) ;
    si.cb = sizeof(si) ;				// 必须是本结构的大小

    // 返回的用于子进程的进程信息
    PROCESS_INFORMATION pi;

    // 利用同样的可执行文件和命令行创建进程，并赋于其子进程的性质
    BOOL bCreateOK=::CreateProcess(
        szFilename,					// 产生这个EXE的应用程序的名称
        szCmdLine,					// 告诉其行为像一个子进程的标志
        NULL,						// 缺省的进程安全性
        NULL,						// 缺省的线程安全性
        FALSE,						// 不继承句柄
        CREATE_NEW_CONSOLE,			// 使用新的控制台
        NULL,						// 新的环境
        NULL,						// 当前目录
        &si,						// 启动信息
        &pi) ;						// 返回的进程信息

    // 
    if (bCreateOK)
    {
        :: CloseHandle(pi.hProcess) ;
        :: CloseHandle(pi.hThread) ;
    }
}

int main(int argc, char* argv[] )
{
    // 
    int nClone(0) ;
    if (argc > 1)
    {
        // 
        :: sscanf(argv[1] , "%d" , &nClone) ;
    }

    // 显示进程位置
    std :: cout << "Process ID:" << :: GetCurrentProcessId()
                << ", Clone ID:" << nClone
                << std :: endl;

    // 
    const int c_nCloneMax=25;
    if (nClone < c_nCloneMax)
    {
        // 
        StartClone(++nClone) ;
    }

    // 在终止之前暂停一下 (l/2秒)
    :: Sleep(500) ;

    return 0;
}
