
#  alter table zlb_wage_info add bank_no varchar(8) null comment '银行行号' after user_phone;
# alter table zlb_wage_info_0 add bank_no varchar(8) null comment '银行行号' after user_phone;
   

before = 'alter table zlb_wage_info_'
after = 'add bank_no varchar(8) null comment "银行行号" after user_phone;'

for i in range(1, 64):
    print(f"{before}{i} {after}")
