#include <iostream>
#include <string>
using namespace std;

int StudentManagementSys()
{
    struct studentInfo
    {
        string firstname;
        string lastname;
        int age;
        char gender;
        string DOB;
        int candidateId;
        string studentInfoList[5];
    };
    studentInfo student0;
    student0.firstname = "Walter";
    student0.lastname = "White";
    student0.age = 17;
    student0.gender = 'M';
    student0.DOB = "27/08/2005";
    student0.candidateId = 195773;
    cout << student0.firstname;
    return 0;
}