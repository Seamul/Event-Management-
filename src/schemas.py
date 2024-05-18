from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import *

# User_Pydantic = pydantic_model_creator(User, name='User')
# UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

DBUser_Pydantic = pydantic_model_creator(DBUser, name='DBUser')
DBUser_Pydantic_In = pydantic_model_creator(DBUser, name='DBUserIn', exclude_readonly=True)
DBUser_Pydantic_Out = pydantic_model_creator(DBUser, name="DBUserOut", exclude=('email'))

UserDevice_Pydantic = pydantic_model_creator(UserDevice, name='UserDevice')
UserDevice_Pydantic_In = pydantic_model_creator(UserDevice, name='UserDeviceIn', exclude_readonly=True)
UserDevice_Pydantic_Out = pydantic_model_creator(UserDevice, name="UserDeviceOut", exclude=('platform'))

UserAuthInfo_Pydantic = pydantic_model_creator(UserAuthInfo, name='UserAuthInfo')
UserAuthInfo_Pydantic_In = pydantic_model_creator(UserAuthInfo, name='UserAuthInfoIn', exclude_readonly=True)
UserAuthInfo_Pydantic_Out = pydantic_model_creator(UserAuthInfo, name='UserAuthInfoOut', exclude=(''))

LoginAttempt_Pydantic = pydantic_model_creator(LoginAttempt, name='LoginAttempt')
LoginAttempt_Pydantic_In = pydantic_model_creator(LoginAttempt, name='LoginAttemptIn', exclude_readonly=True)
LoginAttempt_Pydantic_Out = pydantic_model_creator(LoginAttempt, name='LoginAttemptOut', exclude=(''))