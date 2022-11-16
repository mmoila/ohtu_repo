*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  mikael  secret1234
    Input New Command
    Output Should Contain  New user registered
    
Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Input New Command
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  salasana123
    Input New Command
    Output Should Contain  Username must have at least three lower-case letters

Register With Valid Username And Too Short Password
    Input Credentials  kalle  salasa1
    Input New Command
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  salasana
    Input New Command
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  salasana123