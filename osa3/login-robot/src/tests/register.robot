*** Settings ***
Resource  resource.robot
Test Setup  Reset Application

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input  kalle
    Input  kalle123
    Run Application
    Output Should Contain  New user created

Register With Too Short Username
    Input  new
    Input  ka
    Input  kalle123
    Run Application
    Output Should Contain  Username is too short

Register With Invalid Username Characters
    Input  new
    Input  Kalle
    Input  kalle123
    Run Application
    Output Should Contain  Username must contain only lowercase letters

Register With Too Short Password
    Input  new
    Input  kalle
    Input  kal12
    Run Application
    Output Should Contain  Password is too short

Register With Password Containing Only Letters
    Input  new
    Input  kalle
    Input  salasana
    Run Application
    Output Should Contain  Password must contain numbers or special characters