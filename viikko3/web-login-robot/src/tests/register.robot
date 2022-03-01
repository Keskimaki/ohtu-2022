*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  user
    Set Password  passw0rd
    Set Password Confirmation  passw0rd
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  us
    Set Password  passw0rd
    Set Password Confirmation  passw0rd
    Submit Credentials
    Register Should Fail With Message  Username must be at least three characters long

Register With Valid Username And Too Short Password
    Set Username  user
    Set Password  pass
    Set Password Confirmation  pass
    Submit Credentials
    Register Should Fail With Message  Password must be at least eight characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  passw0rd
    Set Password Confirmation  password
    Submit Credentials
    Register Should Fail With Message  Password and confirmation must match

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open
