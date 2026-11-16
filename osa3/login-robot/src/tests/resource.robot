*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application

Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input  new
    Input  ${username}
    Input  ${password}
    Run Application

Reset Application
    Run Application