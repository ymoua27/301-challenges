#!/usr/bin/env pwsh
# Script:                       Create script that automatically adds AD user
# Author:                       Yue Moua
# Date of latest revision:      12/7/2023
# Purpose:                      Powershell AD automation

Import-Module ActiveDirectory

New-ADUser -SamAccountName "FFerdinand" -Name "FranzFerdinand" -OtherAttributes @{'title'="TPS Reporting Lead";'mail'="ferdi@GlobeXpower.com"}

# Ref
# https://github.com/codefellows/seattle-ops-301d14/blob/main/class-13/challenges/DEMO.md