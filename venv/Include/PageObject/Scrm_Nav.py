from Public.BasePage import BasePage
from selenium.webdriver.common.by import By

class Nav():
    #首页
    home_page_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/li/span')

    #社群管理
    association_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[3]/li/div/span')

    #绑定列表
    association_bind_list_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[1]/li/span')

    #社群Kpl分析
    association_kpl_analyse_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[2]/li/span')

    #社群列表
    association_list_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[3]/li/span')

    #群消息互动
    association_group_message_interact_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[4]/li/span')

    #群发记录
    association_group_send_message_history_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[3]/li/ul/div[5]/li/span')

    #用户管理
    user_manage_loc =(By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[4]/li/div/span')

    #公众号用户
    user_public_user_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[1]/li/span')

    #个号用户
    user_personage_user_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[2]/li/span')

    #平台标签管理
    user_platform_label_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[4]/li/ul/div[3]/li/span')

    #公众号管理
    public_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[5]/li/div/span')

    #公众号列表
    public_list_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div[1]/li/span')

    #粉丝互动
    public_fans_interact_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div[2]/li/span')

    #粉丝互动记录
    public_fans_interact_history_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div[3]/li/span')

    #互动群发
    public_interact_group_send_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div[4]/li/span')

    #互动群发记录
    public_interact_group_send_history_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[5]/li/ul/div[5]/li/span')

    #素材管理
    matter_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/div/span')

    #创建素材
    matter_create_matter_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[1]/li/span')

    #图文素材
    matter_picture_text_matter_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[2]/li/span')

    #图片素材
    matter_picture_matter_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[3]/li/span')

    #快速回复
    matter_fast_reply_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[4]/li/span')

    #小程序素材
    matter_applet_matter_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[5]/li/span')

    #关键词管理
    matter_keyword_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[6]/li/ul/div[6]/li/span')

    #系统管理
    system_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/div/span')

    #用户管理
    system_user_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[1]/li/span')

    #角色管理
    system_role_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[2]/li/span')

    #组织管理
    system_organization_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[3]/li/span')

    #菜单管理
    system_menu_manage_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[4]/li/span')

    #文件上传
    system_file_update_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[5]/li/span')

    #系统日志
    system_log_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[2]/div[1]/div/ul/div[7]/li/ul/div[6]/li/span')
