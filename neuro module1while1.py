base=1#基准生长节点
derive=None#孪生节点空位
cnt=0#时序运算器
trigger=False#布尔闸门开关标记

while not trigger:#外层循环运行规则
    cnt+=1#全局时钟脉冲运算一次
    base +=1#线性自增迭代
    if base ==50:#时序唤醒闸门
        derive=base#把base=50的时序状态复刻给衍生节点
        trigger=True#外层循环的布尔闸门开启
        print(f"触发阈值，衍生数：{derive}")#唤醒日志
        #内层嵌套循环：双数同步迭代
        while base + derive <1000:
            cnt+=1
            base+=1
            derive+=1
        break
print(f"总运算：{cnt} base:{base} derive{derive}")
