'''
Created on 03-Jul-2020
@author: jaspreet
'''
class applicationkeywords():
    def doLogin(self,username, password):
        self.Click("loginlink_xpath")
        self.Type("usernametxtbox_id",username)
        self.Click("nextbtn_xpath")
        self.Type("passwordtxtbox_name",password)
        self.Click("signIn_xpath")
        if(self.isElementPresent("crmlink_xpath")):
            return True 
        else:
            return False
            
        
