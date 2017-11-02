"""
Title: MoreThanAPasswordVault
Developer: Victor Adeshile.
Year: Nov. 1st, 2017.
Accomplices and Co-Developers: UoPeople Computer Science Students GitHub Team.
Tribute: Louai Rahal (CS1101 UoPeople 2017 Instructor)
"""

pinRange = {'Pin':'1,2,3,4,5,6,7,8,9,0', 'Username':'', 'Password':'',}
pin = input('Set up a Pin to get Started: ')
for Pin in pinRange:
    confirm = input('Please Confirm the pin once again: ')
    if pin == confirm:
        print('Your Pin as been successfully set. You Pin is: ', confirm, 'Please, ensure to keep it Safe!')
    else:
        print('Pins do not match.')
