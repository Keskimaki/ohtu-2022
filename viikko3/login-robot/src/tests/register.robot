*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  passw0rd
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  passw0rd
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  us  passw0rd
    Output Should Contain  Username must be at least three characters long

Register With Valid Username And Too Short Password
    Input Credentials  user  pass
    Output Should Contain  Password must be at least eight characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  password
    Output Should Contain  Password must contain a special character

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command
