// proccreate��Ŀ
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
    si.cb = sizeof(si) ;				// �����Ǳ��ṹ�Ĵ�С

    // ���ص������ӽ��̵Ľ�����Ϣ
    PROCESS_INFORMATION pi;

    // ����ͬ���Ŀ�ִ���ļ��������д������̣����������ӽ��̵�����
    BOOL bCreateOK=::CreateProcess(
        szFilename,					// �������EXE��Ӧ�ó��������
        szCmdLine,					// ��������Ϊ��һ���ӽ��̵ı�־
        NULL,						// ȱʡ�Ľ��̰�ȫ��
        NULL,						// ȱʡ���̰߳�ȫ��
        FALSE,						// ���̳о��
        CREATE_NEW_CONSOLE,			// ʹ���µĿ���̨
        NULL,						// �µĻ���
        NULL,						// ��ǰĿ¼
        &si,						// ������Ϣ
        &pi) ;						// ���صĽ�����Ϣ

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

    // ��ʾ����λ��
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

    // ����ֹ֮ǰ��ͣһ�� (l/2��)
    :: Sleep(500) ;

    return 0;
}
