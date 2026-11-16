*** Settings ***
Resource  resource.robot
Test Setup  Reset Application And Create User

*** Test Cases ***
Login With Correct Credentials
    Input  login
    Input Credentials  kalle  kalle123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input  login
    Input Credentials  kalle  vaarasasana
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input  login
    Input Credentials  tuntematon  kalle123
    Output Should Contain  Invalid username or password

*** Keywords ***
Reset Application And Create User
    Input New Command And Create User  kalle  kalle123