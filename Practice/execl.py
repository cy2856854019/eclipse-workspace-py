'''
Created on 2018年11月20日

@author: cy
'''
import xlrd 
#保存结果 
save_file_name="res.txt" 
#待处理数据 
origin_file_name="main.xlsx" 
#保存结果 
res=[] 
#统计每一个timeid对应的和 
tmp_sum=0.0 
last_title="first" 
#读入数据 
wb = xlrd.open_workbook(origin_file_name) 
#打开对应表 
table = wb.sheet_by_index(0) 
#行、列 
nrows = table.nrows 
ncols = table.ncols 
#遍历行 
for index in range(0,nrows): #line 
    lines=table.row_values(index) 
    #获取第一个字段 
    first_field=lines[0] 
    #碰到"timeid=xxxx"这样的行 
    if(str(first_field).find("timeid")!=-1): 
        current_title=str(first_field) 
        if(title!=last_title): 
            #不记录第一个虚timeid 
            if(last_title!="first"): 
                #添加到列表 
                tmp_res=[last_title,round(tmp_sum,2)] 
                res.append(tmp_res) 
            #替换标签，清零 
            last_title=current_title 
            tmp_sum=0.0 
    else: 
        try: #统计和 
            value=float(lines[3]) 
            tmp_sum+=value 
        except Exception as E: 
            print("当前行： "+str(index)) 
            print(str(lines[3])) 
            #保存最后一个        
    if(index==(nrows-1)): 
        tmp_res=[last_title,tmp_sum] 
        res.append(tmp_res) 
        #保存结果到文件 
        with open(save_file_name,"w") as f: 
            for value in res: 
                f.write(str(value[0])+"\t") 
                f.write(str(value[1])) 
                f.write("\n")
