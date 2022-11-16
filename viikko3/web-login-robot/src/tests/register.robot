*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset App And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Registration Should Fail With Message  Username must have at least three lower-case letters
    
Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  salasa3
    Set Password Confirmation  salasa3
    Submit Registration Credentials
    Registration Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  salasa3
    Set Password Confirmation  höpöhöpö
    Submit Registration Credentials
    Registration Should Fail With Message  Password and password confirmation must match


Login After Successful Registration
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Go To Login Page And Log In  kalle  salasana123
    Login Should Succeed

Login After Failed Registration
    Set Username  ka
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration Credentials
    Go To Login Page And Log In  ka  salasana123
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration Credentials
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset App And Go To Register Page
    Reset Application
    Go To Register Page