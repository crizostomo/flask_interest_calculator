# Welcome to the Flask Interest Calculator

## Here it will be explained how you can execute this piece of code


1. ### Installing and Setting Negrok
   1. You need to download ngrok by clicking on this link: 	[https://ngrok.com/download](https://ngrok.com/download)
   2. Unzip the dowloaded file (extension .exe) and put it inside the folder that you created your project
   3. You need to create an account on this website
   4. Follow the steps under "setup & installation", verify in your code if you created a .yml file for ngrok with your authtoken, otherwise create this file in the same folder that it is located your code and insert the authtoken code
2. ### Installing Flask
   1. In your terminal type 'pip install flask'
   2. A message will be displayed that the installation was successful
3. ### Running this code on Windows - Browser
   1. On WINDOWS: Go to your code in your IDE (Visual Studio Code, Pycharm, etc...) and run it
   2. Access your cmd in the admin mode:
      1. Move to the folder that your code is located (for windows you can press 'cd' + the folder path)
      2. Execute the following: ngrok http 5000
      3. It will be generated a https url, for example: https://2a0e-206-0-90-201.ngrok.io
         1. Pick the url address that starts with 'https'
      4. Copy it and paste in the URL address and do not forget to check the route that your code is. For example: https://2a0e-206-0-90-201.ngrok.io/calculator
3. ### Running this code on Windowns - Postman
   1. On WINDOWNS: Go to your code in your IDE (Visual Studio Code, Pycharm, etc...) and run it
   2. Access your cmd in the admin mode:
      1. Move to the folder that your code is located (for windows you can press 'cd' + the folder path)
      2. Execute the following: ngrok http 5000
      3. It will be generated a https url, for example: https://2a0e-206-0-90-201.ngrok.io
         1. Pick the url address that starts with 'https'
      4. Copy it and paste on Postman address do not forget to check the route that your code is. For example: https://2a0e-206-0-90-201.ngrok.io/calculator
      5. Select the option 'POST', 'BODY' and 'JSON'
      6. Input the following:
         1. The three keys that you need to type are: "principal", "interest", and "time".
         2. The values for these keys are your responsibility, the value types are in the next step.
4. ### Inputing the Data
   1. It will be exhibited three key fields (i) Principal, (ii) Annual Interest and (iii) Time
   2. For (i) Principal: 
      1. Type: Float
      2. Put the amount that you would like to calculate
   3. For (ii) Annual Interest: 
      1. Type: Integer
      2. Put the Annual Rate. In this case if you have the monthly rate, just multiply by 12 to have the annual rate
   4. For (iii) Time:
      1. Type: Integer
      2. Put how many years you would like to have your money calculated
5. ### Getting the Result
   1. Hit "Calculate" in browser or "Send" on Postman
   2. It will be showed in R$ how many you are supposed to get
   
   



