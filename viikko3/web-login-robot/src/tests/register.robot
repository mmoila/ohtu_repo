*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Credentials
    Registration Should Fail With Message  Username must have at least three lower-case letters
    
Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  salasa3
    Set Password Confirmation  salasa3
    Submit Credentials
    Registration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  salasa3
    Set Password Confirmation  höpöhöpö
    Submit Credentials
    Registration Should Fail With Message  Password and password confirmation must match
    

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}