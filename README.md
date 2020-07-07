# Whatsapp-Online-Status-Check

### Packages Used

Selenium package for accessing web driver and time package for the time interval between the check.

### Pre Requisites

This is semi-automated program, which involves one time scanning of the QR code for user identification. 

### Installation

1. Install python IDLE
2. Install Selenium by **pip install selenium**
3. Write above code
4. Run the same
5. Web driver opens browser and scan the QR before entering text
6. Input the user
7. Minimise the chrome and keep it in background
8. You will be notified when the user comes online

### How it works

1. Identify the user by span element
2. Check the online status of the user, which is identified by span element 
3. If the user is offline the program gives a exception, which is caught in the program. 
4. The exception caught is identified as user being offline. 
5. Successful execution is identified as user being online. 
6. State values are to be stored, in order to display messages when state is changed. 


